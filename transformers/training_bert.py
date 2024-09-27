#!/usr/bin/env python
#
# training_bert.py
#


# https://www.youtube.com/watch?v=R6hcxMMOrPE
# https://github.com/jamescalam/transformers/blob/main/data/text/meditations/clean.txt


from transformers import BertTokenizer, BertForMaskedLM
import torch


from transformers import logging
logging.set_verbosity_error() # suppress warning message

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased',
                clean_up_tokenization_spaces=True) # avoid deprecation warning

model = BertForMaskedLM.from_pretrained('bert-base-uncased')

with open('meditations.txt', 'r') as fp:
    text = fp.read().split('\n')

print("text:", text[:5])

## tokenize

inputs = tokenizer(text, return_tensors='pt', max_length=512, truncation=True,
                   padding='max_length')


inputs['labels'] = inputs.input_ids.detach().clone()
print("inputs:", inputs)

## masking

rand = torch.rand(inputs.input_ids.shape)
print("rand.shape:", rand.shape)

# mask 15%, avoid special tokens
mask_arr = (rand < 0.15) * (inputs.input_ids != 101) * (inputs.input_ids != 102)

print("mask_arr:", mask_arr)

# tutorial
indices = torch.flatten(mask_arr[0].nonzero()).tolist()
print("indices:", indices)

selection = []

for i in range(mask_arr.shape[0]):
    indices = torch.flatten(mask_arr[i].nonzero()).tolist()
    selection.append(indices)
    
print("selection:", selection)
print("len(selection):", len(selection))

for i in range(mask_arr.shape[0]):
    inputs.input_ids[i, selection[i]] = 103

print("input_ids:", inputs.input_ids)


## data loading

class MeditationsDataset(torch.utils.data.Dataset):
    def __init__(self, encodings):
        self.encodings = encodings

    def __getitem__(self, idx):
        return {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}

    def __len__(self):
        return len(self.encodings.input_ids)


dataset = MeditationsDataset(inputs)

dataloader = torch.utils.data.DataLoader(dataset, batch_size=16, shuffle=True)

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
print("device:", device)

model.to(device)
model.train()

from transformers import AdamW

optim = AdamW(model.parameters(), lr=1e-5)

from tqdm import tqdm

epochs = 2

for epoch in range(epochs):
    loop = tqdm(dataloader, leave=True)
    for batch in loop:
        optim.zero_grad()
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels'].to(device)

        outputs = model(input_ids, attention_mask=attention_mask,
                        labels=labels)

        loss = outputs.loss
        loss.backward()
        optim.step()

        loop.set_description(f'Epoch {epoch}')
        loop.set_postfix(loss=loss.item())


# question:
#
# how does optim.step() update the parameters?  isn't the gradient stored in
# loss?
#
# https://pytorch.org/docs/stable/optim.html
#


# answer from stackoverflow

# Rather than thinking about how loss and parameters are related, you should
# consider them as separate events which are not linked. Indeed, there are two
# distinct elements that have an effect on parameters and their cached
# gradient.

# The autograd mechanism (the process in charge of performing gradient
# computation) allows you to call backward on a torch.Tensor (your loss) and
# which will in turn backpropagate through all the nodes tensors that are
# allowed to compute this final tensor value. Doing so, it will navigate
# through what's called the computation graph, updating each of the parameters'
# gradients by changing their grad attribute. This means that at the end of a
# backward call the network's learned parameters that were used to compute this
# output will have a grad attribute containing the gradient of the loss with
# respect to that parameter.

# loss.backward()

# The optimizer is independent of the backward pass since it doesn't rely on
# it. You can call backward on your graph once, multiple times, or on different
# loss terms depending on your use case. The optimizer's task is to take the
# parameters of the model independently (that is irrespective of the network
# architecture or its computation graph) and update them using a given
# optimization routine (for example via Stochastic Gradient Descent, Root Mean
# Squared Propagation, etc...). It goes through all parameters it was
# initialized with and updates them using their respective gradient value
# (which is supposed to be stored in the grad attribute by at least one
# backpropagation.

# optimizer.step()

# Important notes:

# Keep in mind though that the backward process and the actual update call
# using the optimizer are linked implicitly only by the fact that the optimizer
# will use the results computed by the backward preceding call.

# In PyTorch parameter gradients are kept in memory so you have to clear them
# out before performing a new backward call. This is done using the optimizer's
# zero_grad function. In practice, it clears the grad attribute of the tensors
# it has registered as parameters.





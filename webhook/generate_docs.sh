#!/bin/bash
#
# generate_docs.sh
#

mkdir -p docs
cd docs

#for class in sapiopylib.rest.WebhookService.AbstractWebhookHandler \
#sapiopylib.rest.DataMgmtService.DataMgmtServer \
#sapiopylib.rest.pojo.webhook.WebhookContext.SapioWebhookContext \
#sapiopylib.rest.pojo.webhook.WebhookResult.SapioWebhookResult \
#sapiopylib.rest.WebhookService.WebhookConfiguration \
#sapiopylib.rest.WebhookService.WebhookServerFactory


for class in sapiopylib.rest.WebhookService \
sapiopylib.rest.DataMgmtService \
sapiopylib.rest.pojo.webhook.WebhookContext 
do
    echo $class
    python -m pydoc -w $class 
done



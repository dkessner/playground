#!/bin/bash
#
# generate_docs.sh
#


for class in sapiopylib.rest.WebhookService.AbstractWebhookHandler \
sapiopylib.rest.DataMgmtService.DataMgmtServer \
sapiopylib.rest.pojo.webhook.WebhookContext.SapioWebhookContext \
sapiopylib.rest.pojo.webhook.WebhookResult.SapioWebhookResult \
sapiopylib.rest.WebhookService.WebhookConfiguration \
sapiopylib.rest.WebhookService.WebhookServerFactory
do
    echo $class
    python -m pydoc $class
done



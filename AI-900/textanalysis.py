
import os

# This example requires environment variables named "AZURE_AI_KEY" and "ENDPOINT_TO_CALL_LANGUAGE_API"
AZURE_AI_KEY = "4YS1VpSJFke68rznAluZbWyBa2DtLFSc5g53vmGPHbZk8C48Md8kJQQJ99CDACHYHv6XJ3w3AAAAACOGuD0C"
ENDPOINT_TO_CALL_LANGUAGE_API ="https://ai-tripathiprasoon9917ai730173429272.openai.azure.com/"
#key = os.environ.get('AZURE_AI_KEY')
#endpoint = os.environ.get('ENDPOINT_TO_CALL_LANGUAGE_API')
key = AZURE_AI_KEY
endpoint = ENDPOINT_TO_CALL_LANGUAGE_API

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Authenticate the client using your key and endpoint 
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()
#Example  2: Extractive summarization
# Example method for summarizing text
def sample_extractive_summarization(client):
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import (
        TextAnalyticsClient,
        ExtractiveSummaryAction
    ) 


 #  document = [
 #        "The extractive summarization feature uses natural language processing techniques to locate key sentences in an unstructured text document. "
 #       "These sentences collectively convey the main idea of the document. This feature is provided as an API for developers. " 
 #       "They can use it to build intelligent solutions based on the relevant information extracted to support various use cases. "
 #       "Extractive summarization supports several languages. It is based on pretrained multilingual transformer models, part of our quest for holistic representations. "
 #       "It draws its strength from transfer learning across monolingual and harness the shared nature of languages to produce models of improved quality and efficiency. "
 #   ]

    document = [
        "Unit 4 of 7, Azure Language MCP. An AI agent uses tools and models to perform tasks such as reasoning, planning, retrieval, and calling external services. While AI agents can use various generative AI models to perform the language-related tasks, you can create an agent that uses Azure Foundry and Foundry tools to ensure consistent and predictable text analysis functionality. The Azure Language MCP server in Foundry tool is a managed service that exposes Azure language capabilities through the model context protocol so that AI agents can use advanced language processing tools without custom integration work. MCP. An MCP server gives an agent access to the tools, data, or action that the agent cannot do on its own. The agent can make a request to the MCP server. The MCP server might respond by providing the data, for example, files or calls for analytics, taking the actions, for example, sending an email. You can access the Azure Language MCP servers and other Foundry tools in the new Foundry portal, Azure Language in the Foundry tool, Azure Language in the Foundry capabilities. MCP server enables AI agents to seamlessly access the capabilities of Azure Language in Foundry tools through the standardized MCP endpoints to achieve more accurate, explainable, and compliant outcomes with PII, redaction, language detection, custom question answering, and more."        
    ]

    poller = client.begin_analyze_actions(
        document,
        actions=[
            ExtractiveSummaryAction(max_sentence_count=4)
        ],
    )

    document_results = poller.result()
    for result in document_results:
        extract_summary_result = result[0]  # first document, first result
        if extract_summary_result.is_error:
            print("...Is an error with code '{}' and message '{}'".format(
                extract_summary_result.code, extract_summary_result.message
            ))
        else:
            print("Summary extracted:{}".format(
                " ".join([sentence.text for sentence in extract_summary_result.sentences]))
            )

sample_extractive_summarization(client)


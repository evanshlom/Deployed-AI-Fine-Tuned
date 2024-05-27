from mistral.client import MistralClient

from fine_tuning_data_prep import prepare_documents

# initialize the Mistral client with your API key
client = MistralClient('YOUR_API_KEY')

# prepare your data as a list of dictionaries, with "prompt" and "completion" keys
data = [
    {"prompt": "prompt1", "completion": "completion1"},
    {"prompt": "prompt2", "completion": "completion2"},
    ...
]

# upload your data as a dataset
dataset_id = client.create_dataset(name='my_dataset', data=data)

# set up the fine-tuning job
job = client.fine_tune(
    model_name='base-model-name',
    dataset_id=dataset_id,
    name='my_fine_tuned_model'
)

# wait for the fine-tuning job to complete
job.wait()
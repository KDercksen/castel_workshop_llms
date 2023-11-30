In the examples for this workshop, we will use the OpenAI and Together APIs.
For both of these, you need an API key. You can get an OpenAI API key
[here](https://platform.openai.com/). You can get a Together API key
[here](https://api.together.xyz/).

Create a `.env` file in the root directory of this project and add the
following:

```bash
# .env
OPENAI_API_KEY=<your key here>
TOGETHER_API_KEY=<your key here>
```

Install the required Python dependencies (inside a virtual environment):

```bash
pip install -r requirements.txt
```

### Scripts included

| Script                | Description                                                                                              |
| --------------------- | -------------------------------------------------------------------------------------------------------- |
| make_data.py          | Create a dataset of short stories using ChatGPT. The data from this script is used in `estimate_cost.py` |
| estimate_cost.py      | Estimate the cost of generating a set of short stories using ChatGPT. Run `make_data.py` first.          |
| how_to_prompt.py      | Examples of querying OpenAI and Together.AI LLMs through API.                                            |
| modalities_plot.ipynb | Simulation of cost and duration of serverless vs dedicated machine.                                      |

### Resources

- [OpenAI](https://openai.com/)
- [Together](https://together.ai/)
- [Huggingface](https://huggingface.co/)
- [LangChain](https://python.langchain.com/docs/get_started/introduction) (chaining LLMs and other applications together for more complicated tasks)

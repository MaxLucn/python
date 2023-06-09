import { Configuration, OpenAIApi } from "openai";
const configuration = new Configuration({
    organization: "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",
    apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);
const response = await openai.listEngines();
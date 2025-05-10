import { ChatGroq } from "@langchain/groq";
import { ChatPromptTemplate } from "@langchain/core/prompts"
import { config } from "dotenv";
config();

let llm = new ChatGroq({
  model: "llama-3.3-70b-versatile",
  temperature: 0,
  maxTokens: undefined,
  maxRetries: 2,
});

let prompt_template = ChatPromptTemplate.fromMessages([
  ['system',"You are a helpful assistant and you can manage what things we should bring when we go trips based on Location and Days."],
  ['user', "What should I bring, I be going to {location} within {days}"]
]);

// console.log(await prompt_template.invoke({'location': 'bagan', "days": "5/10/2025 to 5/15/2025"}))

let pipeline = prompt_template.pipe(llm)

console.log(await pipeline.invoke({'location': "bagan", "days": "5/10/2025 to 5/15/2025"}));

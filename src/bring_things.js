import { ChatGroq } from "@langchain/groq";

import { config } from "dotenv";
config();

const llm = new ChatGroq({
  GROQ_API_KEY: process.env.GROQ_API_KEY,
  model: "llama-3.3-70b-versatile",
  temperature: 0,
  maxTokens: undefined,
  maxRetries: 2,
});

const aiMsg = await llm.invoke([
    {
      role: "system",
      content:
        "You are a helpful assistant.",
    },
    { role: "user", content: "How to learn programming with only one language." },
  ]);
console.log(aiMsg['content']);
import { GoogleGenAI, Type } from "@google/genai";
import { StudySession } from "../types";

const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY || "" });

export async function explainConcept(
  concept: string, 
  language: string, 
  image?: string
): Promise<{ explanation: string; analogy: string }> {
  const parts: any[] = [
    { text: `You are SomaAI, a brilliant STEM tutor for students in East Africa. 
    Explain the following concept: "${concept}".
    
    Rules:
    1. Use code-switching between English and ${language} (Swahili or Sheng). If the language is Sheng, use modern, urban Sheng that students relate to.
    2. Provide a highly localized analogy relevant to East African life. Think about:
       - Farming (shamba, maize, coffee)
       - Cooking (ugali, sukuma wiki, jiko)
       - Transport (matatus, boda bodas, SGR)
       - Market trade (mama mboga, bargaining, kiosks)
       - Sports (football, athletics)
       - Nature (savannah, wildlife, Rift Valley)
    3. Keep it encouraging, simple, and conversational.
    
    Return the response as JSON with "explanation" and "analogy" fields.` }
  ];

  if (image) {
    parts.push({
      inlineData: {
        mimeType: "image/jpeg",
        data: image.split(',')[1]
      }
    });
  }

  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: { parts },
    config: {
      responseMimeType: "application/json",
      responseSchema: {
        type: Type.OBJECT,
        properties: {
          explanation: { type: Type.STRING },
          analogy: { type: Type.STRING },
        },
        required: ["explanation", "analogy"],
      },
    },
  });
  
  return JSON.parse(response.text);
}

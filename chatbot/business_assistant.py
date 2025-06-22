import groq
from typing import List, Dict

class BusinessAssistant:
    def __init__(self):
        self.client = groq.Groq(api_key='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')
        self.contexts = {
            "customer_support": """You are a customer support specialist helping small businesses handle customer inquiries.
            Focus on providing professional, helpful responses for common customer service scenarios.""",
            
            "business_advice": """You are a business consultant providing strategic advice to small businesses.
            Focus on practical, actionable insights for business growth and optimization.""",
            
            "financial_guidance": """You are a financial advisor helping small businesses with financial decisions.
            Provide guidance on budgeting, pricing, and financial planning.""",
            
            "marketing_strategy": """You are a marketing strategist helping small businesses with their marketing efforts.
            Offer practical marketing advice and campaign suggestions."""
        }

    def get_response(self, message: str, context_type: str = "business_advice") -> str:
        try:
            context = self.contexts.get(context_type, self.contexts["business_advice"])
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": context},
                    {"role": "user", "content": message}
                ],
                model="mixtral-8x7b-32768",
                temperature=0.7,
                max_tokens=1024
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"
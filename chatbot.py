from transformers import AutoTokenizer, AutoModelForCausalLM

class Phi2Chatbot:
    def __init__(self):
        model_name = "microsoft/phi-2"
        print("Loading model... (this may take a minute)")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        # Set pad_token to eos_token (or any other token you prefer)
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
        
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        print("Model loaded.")

    def generate_response(self, user_input: str) -> str:
        prompt = (
            f"### Instruction:\nYou are a helpful AI assistant. Respond conversationally.\n\n"
            f"### Input:\n{user_input}\n\n### Response:\n"
        )

        inputs = self.tokenizer(prompt, return_tensors="pt", padding=True)
        input_ids = inputs["input_ids"]
        attention_mask = inputs["attention_mask"]

        output = self.model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_new_tokens=200,
            pad_token_id=self.tokenizer.eos_token_id  # Using eos_token_id as pad_token_id
        )

        decoded = self.tokenizer.decode(output[0], skip_special_tokens=True)

        if "### Response:" in decoded:
            return decoded.split("### Response:")[-1].strip()
        else:
            return decoded.strip()

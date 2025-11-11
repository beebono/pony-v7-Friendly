import torch
from comfy import model_management as mm
from comfy.comfy_types import IO

class T5Balancer:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "conditioning": (IO.CONDITIONING, {"tooltip": "The positive conditioning to analyze."})
            }
        }

    RETURN_TYPES = (IO.CONDITIONING, "INT")
    RETURN_NAMES = ("conditioning_passthrough", "token_length")
    FUNCTION = "analyze"
    CATEGORY = "conditioning"

    def analyze(self, conditioning):
        seq_len = 0

        try:
            if isinstance(conditioning, list) and len(conditioning) > 0:
                first = conditioning[0]
                if isinstance(first, list) and len(first) > 0:
                    tensor = first[0]
                    if isinstance(tensor, torch.Tensor):
                        seq_len = tensor.shape[1]
                        print(f"[T5Balancer] Detected token length: {seq_len}")
        except Exception as e:
            print(f"[T5Balancer] Failed to get token length: {e}")

        return (conditioning, int(seq_len))

NODE_CLASS_MAPPINGS = {
    "T5Balancer": T5Balancer
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "T5Balancer": "T5 Token Length Balancer"
}
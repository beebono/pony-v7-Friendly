# pony-v7-Friendly

**An attempt at more amicable ComfyUI workflows for working with `pony-v7-base`.**

---

## Features

- **Foundational fun**  
  Links to the necessary files for generation are included in the workflow, along with some starter style cluster tags to get you going.

- **Simple and clean**  
  Start your prompt with `score_9` and a `style_cluster_x`, then add a short sentence describing what you want to see. No need for chapters of fanfiction, just results!

- **Power to the prompter**  
  Negative prompts usually aren’t needed, but you can still try one out if you want to refine certain results.

- **Options abound**  
  Don't want to install more than you absolutely have to? Try the Lite workflow! It'll probably take a bit longer, but it's not THAT bad...

---

## The Secret Ingredients

1. Your prompt is expanded to fill most of the context window in `pony-v7-base` using a **T5TokenizerOptions** node with `min_length` set to **768**.
2. A simple custom node called **T5 Token Length Balancer** reads how many tokens were produced by the **Positive Prompt** encoding (typically 768) and pads the **Negative Prompt** accordingly, keeping both in harmony.
3. (Non-Lite) The **RES4LYF ClownsharKSampler** sprinkles in its unique diffusion magic for extra efficiency. (Don’t ask how, it’s wizardry to me. Maybe real unicorns are involved?)
4. **Love** and **Friendship**, duh.

---

## Requirements

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- HIGHLY recommended, but not required with the Lite workflow:
  - [RES4LYF Custom Nodes](https://github.com/ClownsharkBatwing/RES4LYF)

---

## Installation & Usage


1. Download and place `t5_token_balancer.py` from this repository into your `custom_nodes` folder.  
2. (Non-Lite) Install **RES4LYF** in your `ComfyUI/custom_nodes/` directory by following the instructions in the linked repository.  
3. Restart ComfyUI if it’s already running.  
4. Load the workflow by either:
   - Opening `pony-v7-Friendly(-Lite).json`, **or**
   - Dragging and dropping `pony-v7-Friendly(-Lite).png` onto your ComfyUI canvas.  
5. Make some magic happen!

---

## License

```
MIT License

Copyright (c) 2025 Noxwell (beebono)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights 
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
copies of the Software, and to permit persons to whom the Software is 
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in 
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN 
THE SOFTWARE.
```

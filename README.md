# 🌞 Superklok Labs Non-Commercial ComfyUI DEMO v1.0.0

Welcome to the official **Superklok Labs** public open-source ComfyUI demonstration repository. This repository provides access to our production-grade pipeline utilized to build, iterate, and stylize the core character asset of the **TrenchPetals** universe: **Sunny Chuxem**.

⚠️ **Licensing & Usage Note:** This demonstration environment is distributed under the **Superklok Labs Non-Commercial Demo Asset License v1.0** due to core model dependencies falling under non-commercial restrictions. These workflows are intended exclusively for educational, research, and evaluation purposes. For full trademark, asset rules, and multi-platform attribution policies, please review the accompanying `LICENSE` file.

---

## 📋 Key Pipeline Features Demonstrated

*   **Advanced Impact Pack Integration:** Features a triple-tier detailing assembly leveraging targeted `FaceDetailer`, `HandDetailer`, and `FootDetailer` nodes to automatically enforce precise cell-shaded lines and lock down the character's signature 1980s rubber-hose aesthetic.
*   **Centralized Master Switch Logic:** Outlines our modular configuration topology using an integrated `ImpactSwitch` array linked to a main `MASTER SWITCH` primitive node. This allows developers to toggle between complex prompt pipelines and distinct layout configurations instantly without structural breakages.
*   **Rectified Flow Negative Conditioning:** Demonstrates high-precision formatting tricks for text conditioning layers using specialized `FluxGuidance` nodes to correctly inject structural negative overrides within the transformer stack.

---

## 🏗️ Repository Architecture & Workflows

This toolkit includes two discrete operational pipelines mapped directly to their respective architectural generations:

### 1. FLUX 2 Klein Evaluation Pipeline
*   **Workflow File:** `NonCommercialDEMO - Img2Img + Txt2Img Flux2Klein Multi-Workflow.json`
*   **Core Checkpoint Target:** `flux-2-klein-9b-fp8.safetensors`
*   **Text Encoder Requirement:** `qwen_3_8b_fp8mixed.safetensors`
*   **Detailing Pass Profile:** 15 localized steps utilizing custom `karras` scheduler hooks.

### 2. FLUX 3 Image Klein Production Pipeline
*   **Workflow File:** `NonCommercialDEMO - Img2Img + Txt2Img Flux3Klein Multi-Workflow.json`
*   **Core Checkpoint Target:** `flux3-image-klein-int8-convrot.safetensors`
*   **Text Encoder Requirement:** `flux-3-image-klein-text_encoder-FP8.safetensors`
*   **Detailing Pass Profile:** 20 localized steps running on synchronized `beta` scheduling logic for ultra-crisp resolution upscaling.

---

## 💵 Need Commercial Production-Grade Solutions?

While this public repository showcases our foundational framework under non-commercial terms, **Superklok Labs** designs and builds bespoke, 100% commercially unrestricted, high-throughput studio pipelines engineered for studio deployments and enterprise AI art generation.

If you want to secure a custom, optimized node ecosystem for your brand or license advanced, commercial-ready toolkits, let's collaborate:

* 💼 **Hire on [Upwork](https://www.upwork.com/freelancers/~01a2b86360ffeb733e)**
* ⚡ **Hire on [Contra](https://contra.com/Superklok)**
* 🌐 **Portfolio on [GitHub](https://github.com/Superklok)**
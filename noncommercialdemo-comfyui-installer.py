#!/usr/bin/env python3
"""
⚡ Superklok Labs — NonCommercialDEMO Core Architecture Platform Installer ⚡
Author: Trevor Morin | Superklok Labs ➔ superklok.com
License: Superklok Labs Non-Commercial Demo Asset License v1.0

This highly advanced platform installer designs a fully integrated local FLUX.2 / FLUX 3 Klein pipeline.
Deploys an unprivileged portable workspace for ComfyUI with Impact Pack, Ultralytics, and Klein weights.
"""

import os
import sys

# -------------------------------------------------------------------------
# GLOBAL UX ENVIRONMENTAL OVERRIDES
# Must be set first before any third-party framework evaluations occur
# -------------------------------------------------------------------------
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"

import shutil
import urllib.request
import subprocess
import threading
import time

# -------------------------------------------------------------------------
# DEPENDENCY HANDSHAKE & RUNTIME INJECTION
# Handled first to ensure modules are ready before core script evaluation
# -------------------------------------------------------------------------
REQUIRED_LIBS = ["rich", "py7zr"]
missing_libs = []

for lib in REQUIRED_LIBS:
    try:
        __import__(lib)
    except ImportError:
        missing_libs.append(lib)

if missing_libs:
    done = False
    
    def animate_bootstrap():
        # A dynamic array of high-grade console frame indicators
        frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        idx = 0
        while not done:
            sys.stdout.write(f"\r\033[95m{frames[idx % len(frames)]}\033[0m Preparing Superklok core engine libraries (allocating visual assets)...")
            sys.stdout.flush()
            time.sleep(0.08)
            idx += 1
        sys.stdout.write("\r" + " " * 85 + "\r")
        sys.stdout.flush()

    # Spins up the animation loop on a concurrent background worker thread
    anim_thread = threading.Thread(target=animate_bootstrap, daemon=True)
    anim_thread.start()

    try:
        # Silently downloads the design wheels using completely hidden null routing parameters
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", *missing_libs, "--quiet", "--no-warn-script-location", "--user"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    finally:
        # Halt the loop thread immediately when pip closes
        done = True
        anim_thread.join()
    
    # Inject user-site packages into the runtime system path
    import site
    if hasattr(site, 'getusersitepackages'):
        user_site = site.getusersitepackages()
        if user_site not in sys.path:
            sys.path.insert(0, user_site)

from rich.console import Console
from rich.panel import Panel
from rich.status import Status
from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    BarColumn,
    TaskProgressColumn,
    DownloadColumn,
    TransferSpeedColumn,
    TimeRemainingColumn,
)
import py7zr

# Initialize global styling console
console = Console()

class NonCommercialDemoInstaller:
    """Orchestrates ComfyUI pipeline architecture configurations for FLUX.2 & FLUX 3 Klein workflows."""

    # Flux2Klein 9B FP8 Checkpoint (ungated public mirror)
    FLUX2_KLEIN_MODEL_URL: str = (
        "https://huggingface.co/CrocodileBanana/2026.03.01/resolve/main/flux-2-klein-9b-fp8.safetensors"
    )

    # Flux2Klein Text Encoder (Qwen 3 8B FP8 Mixed)
    FLUX2_TEXT_ENCODER_URL: str = (
        "https://huggingface.co/Comfy-Org/Flux-2-Klein-9B/resolve/main/split_files/text_encoders/qwen_3_8b_fp8mixed.safetensors"
    )

    # Flux 3 Image Klein INT8 ConvRot Checkpoint (ungated public mirror)
    FLUX3_KLEIN_MODEL_URL: str = (
        "https://huggingface.co/LS110824/Flux3/resolve/main/flux3-image-klein-int8-convrot.safetensors"
    )

    # Flux 3 Image Klein FP8 Text Encoder (ungated public mirror)
    FLUX3_TEXT_ENCODER_URL: str = (
        "https://huggingface.co/unsloth/flux-3-image-klein-FP8/resolve/0e7c103d8ffafb0d4ccd8d82122375c878cdaf4d/flux-3-image-klein-text_encoder-FP8.safetensors"
    )

    # Shared FLUX.2 & FLUX 3 VAE Encoder/Decoder
    FLUX2_VAE_URL: str = (
        "https://huggingface.co/ai-toolkit/flux2_vae/resolve/main/ae.safetensors"
    )

    # Segment Anything Model (SAM) Edge Tracker weight link
    SAM_MODEL_URL: str = (
        "https://huggingface.co/ybelkada/segment-anything/resolve/main/checkpoints/sam_vit_h_4b8939.pth"
    )

    # Ultralytics YOLO BBOX Detectors for Face, Hand, and Foot Detailers
    FACE_YOLO_URL: str = (
        "https://huggingface.co/Bingsu/adetailer/resolve/main/face_yolov8n_v2.pt"
    )
    HAND_YOLO_URL: str = (
        "https://huggingface.co/Bingsu/adetailer/resolve/main/hand_yolov9c.pt"
    )
    FOOT_YOLO_URL: str = (
        "https://huggingface.co/MonetEinsley/ADetailer_CM/resolve/main/foot_yolov8x_v2.pt"
    )
    
    # ComfyUI Official standalone portable build asset link
    COMFYUI_PORTABLE_URL: str = (
        "https://github.com/comfyanonymous/ComfyUI/releases/latest/download/ComfyUI_windows_portable_nvidia.7z"
    )

    def __init__(self) -> None:
        # Resolve all top-level platform layers relative to workspace footprint
        self.root_dir: str = os.getcwd()
        
        # Generation Spaces (nested inside Image-Generation per NonCommercialDEMO structure)
        self.img_gen_dir: str = os.path.join(self.root_dir, "Image-Generation")
        self.archive_path: str = os.path.join(self.img_gen_dir, "ComfyUI_windows_portable_nvidia.7z")
        self.portable_dir: str = os.path.join(self.img_gen_dir, "ComfyUI_windows_portable")
        self.comfy_dir: str = os.path.join(self.portable_dir, "ComfyUI")
        self.nodes_dir: str = os.path.join(self.comfy_dir, "custom_nodes")

    def render_welcome_banner(self) -> None:
        """Displays a styled branding header into the active terminal session."""
        banner_text = (
            "[bold yellow]🌞 NonCommercialDEMO v.1.97.0 — Non-Commercial Image-Generation DEMO 🌞[/bold yellow]\n"
            "[bold cyan]Author: Trevor Morin | Superklok Labs ➔ superklok.com[/bold cyan]\n\n"
            "[dim]Installer configures low-VRAM FP8 rendering, clones Impact & Ultralytics detailers,\n"
            "streams FLUX.2 & FLUX 3 Klein weights, and injects character canvases natively.[/dim]"
        )
        console.print(Panel.fit(banner_text, border_style="cyan", padding=(1, 4)))

    def stream_large_file(self, url: str, dest_path: str, description: str) -> None:
        """Downloads heavy binary layers utilizing multi-threaded concurrent chunk segmenting with atomic .part safeguards."""
        import concurrent.futures
        import threading

        if os.path.exists(dest_path):
            console.print(f"[bold green]✓[/bold green] {os.path.basename(dest_path)} detected in cache. Skipping download.")
            return

        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        temp_path = f"{dest_path}.part"

        if os.path.exists(temp_path):
            try:
                os.remove(temp_path)
            except OSError:
                pass

        progress_lock = threading.Lock()

        with Progress(
            SpinnerColumn(spinner_name="dots", style="bright_cyan"),
            TextColumn(description),
            BarColumn(
                bar_width=45,
                style="black on blue",
                complete_style="magenta",
                finished_style="green",
                pulse_style="magenta"
            ),
            TaskProgressColumn(style="bold yellow"),
            DownloadColumn(binary_units=True),
            TransferSpeedColumn(),
            TimeRemainingColumn(),
            console=console,
            refresh_per_second=20,
            auto_refresh=True
        ) as progress:

            task_id = progress.add_task(description="", total=None)

            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}, method='HEAD')
                with urllib.request.urlopen(req) as resp:
                    total_size = int(resp.info().get('Content-Length', 0))
            except Exception:
                total_size = 0

            if total_size == 0:
                try:
                    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
                    with urllib.request.urlopen(req) as response:
                        total_size = int(response.info().get('Content-Length', 0))
                        progress.update(task_id, total=total_size)
                        with open(temp_path, 'wb') as f:
                            while chunk := response.read(1024 * 128):
                                f.write(chunk)
                                progress.update(task_id, advance=len(chunk))
                        os.replace(temp_path, dest_path)
                        return
                except Exception as e:
                    console.print(f"[bold red]❌ Fallback Stream Interrupted: {e}[/bold red]")
                    sys.exit(1)

            num_threads = 4
            chunk_size = total_size // num_threads
            ranges = []
            for i in range(num_threads):
                start = i * chunk_size
                end = total_size - 1 if i == num_threads - 1 else (start + chunk_size - 1)
                ranges.append((start, end))

            with open(temp_path, 'wb') as f:
                f.truncate(total_size)

            progress.update(task_id, total=total_size)

            def download_range(part_num, start, end):
                req = urllib.request.Request(url, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                    'Range': f'bytes={start}-{end}'
                })
                try:
                    with urllib.request.urlopen(req) as response:
                        with open(temp_path, 'r+b') as f:
                            f.seek(start)
                            buffer_size = 1024 * 64
                            while chunk := response.read(buffer_size):
                                f.write(chunk)
                                with progress_lock:
                                    progress.update(task_id, advance=len(chunk))
                except urllib.error.HTTPError as e:
                    if e.code == 501 or e.code == 416:
                        with progress_lock:
                            raise NotImplementedError("Range unsupported")
                    console.print(f"\n[bold red]❌ Thread {part_num} dropped stream: {e}[/bold red]")
                    os._exit(1)
                except Exception as e:
                    console.print(f"\n[bold red]❌ Thread {part_num} dropped stream: {e}[/bold red]")
                    os._exit(1)

            try:
                with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
                    futures = [
                        executor.submit(download_range, idx, r[0], r[1])
                        for idx, r in enumerate(ranges)
                    ]
                    for future in concurrent.futures.as_completed(futures):
                        future.result()
                os.replace(temp_path, dest_path)
            except (NotImplementedError, concurrent.futures.BrokenExecutor):
                try:
                    os.remove(temp_path)
                except OSError:
                    pass
                
                progress.update(task_id, total=None)
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
                try:
                    with urllib.request.urlopen(req) as response:
                        total_size = int(response.info().get('Content-Length', 0))
                        progress.update(task_id, total=total_size)
                        with open(temp_path, 'wb') as f:
                            while chunk := response.read(1024 * 128):
                                f.write(chunk)
                                progress.update(task_id, advance=len(chunk))
                        os.replace(temp_path, dest_path)
                except Exception as e:
                    console.print(f"[bold red]❌ Fallback Stream Interrupted: {e}[/bold red]")
                    sys.exit(1)

    def extract_portable_environment(self) -> None:
        """Unpacks the standalone environment package dynamically utilizing an auto-fetched 7zr helper."""
        if os.path.exists(self.portable_dir):
            console.print("[bold green]✓[/bold green] ComfyUI Portable framework directory structure already initialized.")
            return

        if not os.path.exists(self.archive_path):
            console.print(f"[bold red]❌ Extraction payload missing: {self.archive_path}[/bold red]")
            sys.exit(1)

        with Status("[bold white]Decompressing ComfyUI Core Environment (Native Hardware Pipeline)...[/bold white]", console=console, spinner="bouncingBall") as status:
            try:
                archive_abs = os.path.abspath(self.archive_path)
                img_gen_abs = os.path.abspath(self.img_gen_dir)
                
                extractor_bin = os.path.join(self.img_gen_dir, "7zr.exe")
                if not os.path.exists(extractor_bin):
                    primary_url = "https://www.7-zip.org/a/7zr.exe"
                    fallback_url = "https://github.com/ip7z/7zip/releases/download/26.06/7zr.exe"
                    try:
                        urllib.request.urlretrieve(primary_url, extractor_bin)
                    except Exception:
                        urllib.request.urlretrieve(fallback_url, extractor_bin)
                
                subprocess.run(
                    [extractor_bin, "x", archive_abs, f"-o{img_gen_abs}", "-y"],
                    check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
                )
                
                extracted_expected = os.path.join(self.img_gen_dir, "ComfyUI_windows_portable_nvidia")
                if os.path.exists(extracted_expected) and not os.path.exists(self.portable_dir):
                    os.rename(extracted_expected, self.portable_dir)
                    
                console.print("[bold green]✓[/bold green] Standalone visual environment successfully unpacked.")
                
                try:
                    os.remove(self.archive_path)
                    if os.path.exists(extractor_bin):
                        os.remove(extractor_bin)
                except OSError:
                    pass
            except Exception as e:
                console.print(f"[bold red]❌ Failed unpacking portable suite via hardware layout: {e}[/bold red]")
                sys.exit(1)

    def execute_git_clone(self, repo_url: str, base_destination: str, folder_name: str, name_label: str) -> None:
        """Safely forks public version-controlled extensions into target terminal paths."""
        target_path = os.path.join(base_destination, folder_name)
        if os.path.exists(target_path):
            console.print(f"[bold green]✓[/bold green] [bold yellow]{name_label}[/bold yellow] already linked in workspace.")
            return

        with Status(f"[bold white]Cloning {name_label}...[/bold white]", console=console, spinner="aesthetic") as status:
            try:
                subprocess.run(
                    ["git", "clone", repo_url, target_path],
                    check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
                )
                console.print(f"[bold green]✓[/bold green] Installed [bold cyan]{name_label}[/bold cyan] to production folders.")
            except (subprocess.CalledProcessError, FileNotFoundError):
                console.print(f"[bold red]❌ Failed tracking Git dependency. Ensure Git for Windows is installed globally.[/bold red]")
                sys.exit(1)

    def provision_launch_scripts(self) -> None:
        """Injects custom startup code configured for low-VRAM FP8 memory balancing directly into runtime paths."""
        startup_file = os.path.join(self.portable_dir, "run_nvidia_gpu.bat")
        
        # Specialized balancing constraints tailored for single 16GB VRAM card limits
        optimized_args = (
            ".\\python_embeded\\python.exe -s ComfyUI\\main.py --windows-standalone-build "
            "--fp8_e4m3fn-text-enc --use-pytorch-cross-attention --lowvram\n"
        )

        try:
            with open(startup_file, "w", encoding="utf-8") as file:
                file.write(optimized_args)
            console.print("[bold green]✓[/bold green] Low-overhead VRAM arguments written to launch script.")
        except IOError:
            console.print("[bold red]❌ Launch script adjustment error.[/bold red]")

    def inject_comfyui_inputs(self) -> None:
        """Copies character reference skins and widescreen canvas PNG assets into ComfyUI's input directory."""
        comfy_input_dir = os.path.join(self.comfy_dir, "input")
        os.makedirs(comfy_input_dir, exist_ok=True)

        candidate_folders = [
            os.path.join(self.root_dir, "Assets"),
            os.path.join(self.img_gen_dir, "Assets"),
            os.path.join(self.root_dir, "Sunny Chuxem Character Info", "Skins"),
            os.path.join(self.root_dir, "Benchmark Character - Sunny Chuxem", "Skins"),
        ]

        copied_count = 0
        for folder in candidate_folders:
            if os.path.exists(folder):
                for file in sorted(os.listdir(folder)):
                    if file.lower().endswith(".png"):
                        src_path = os.path.join(folder, file)
                        dest_path = os.path.join(comfy_input_dir, file)
                        if not os.path.exists(dest_path):
                            shutil.copy2(src_path, dest_path)
                        copied_count += 1

        if copied_count > 0:
            console.print(f"[bold green]✓[/bold green] Loaded {copied_count} character & canvas PNG assets into ComfyUI\\input.")
        else:
            console.print("[bold yellow]⚠[/bold yellow] Reference PNG files were not found in Assets or Skins directories.")

    def run(self) -> None:
        """Executes orchestration steps sequentially."""
        self.render_welcome_banner()

        # Step 1: Initialize Image-Generation Directory Tree & Fetch ComfyUI Portable
        os.makedirs(self.img_gen_dir, exist_ok=True)
        if not os.path.exists(self.portable_dir) and not os.path.exists(self.archive_path):
            self.stream_large_file(
                url=self.COMFYUI_PORTABLE_URL,
                dest_path=self.archive_path,
                description="[bold white]Streaming ComfyUI Portable Build[/bold white]"
            )

        # Step 2: Unpack ComfyUI Base Layer Environment
        self.extract_portable_environment()

        # Step 3: Inject Optimized Drivers & Hardware Controls
        self.provision_launch_scripts()

        # Step 4: Provision Node Ecosystem Extension Networks
        console.print("\n[bold magenta]» Linking Specialized Multi-Modal ComfyUI Nodes...[/bold magenta]")
        node_extensions = {
            "comfyui-manager": "https://github.com/ltdrdata/ComfyUI-Manager",
            "ComfyUI-Impact-Pack": "https://github.com/ltdrdata/ComfyUI-Impact-Pack",
            "ComfyUI-Impact-Subpack": "https://github.com/ltdrdata/ComfyUI-Impact-Subpack",
            "ComfyUI-Inspire-Pack": "https://github.com/ltdrdata/ComfyUI-Inspire-Pack",
            "comfyui_controlnet_aux": "https://github.com/Fannovel16/comfyui_controlnet_aux"
        }
        for folder, url in node_extensions.items():
            self.execute_git_clone(repo_url=url, base_destination=self.nodes_dir, folder_name=folder, name_label=folder)

        # Initializing Node Pack Dependencies via Embedded Python
        console.print("\n[bold magenta]» Initializing Node Pack Dependencies via Embedded Python...[/bold magenta]")
        embedded_python = os.path.join(self.portable_dir, "python_embeded", "python.exe")
        
        if os.path.exists(embedded_python):
            # Explicitly force-upgrade ComfyUI-Manager requirements first to ensure stable mapping
            manager_req = os.path.join(self.nodes_dir, "comfyui-manager", "requirements.txt")
            if os.path.exists(manager_req):
                with Status("[bold white]Securing ComfyUI-Manager requirements...[/bold white]", console=console) as status:
                    subprocess.run([embedded_python, "-m", "pip", "install", "--no-warn-script-location", "--isolated", "-r", manager_req, "--quiet"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            # Bypass internal install.py routing entirely and force pip execution over all complex node requirements
            complex_nodes = [
                "ComfyUI-Impact-Pack",
                "ComfyUI-Impact-Subpack",
                "ComfyUI-Inspire-Pack",
                "comfyui_controlnet_aux"
            ]
            for node_folder in complex_nodes:
                requirements_txt = os.path.join(self.nodes_dir, node_folder, "requirements.txt")
                
                if os.path.exists(requirements_txt):
                    with Status(f"[bold white]Compiling environment libraries for {node_folder}...[/bold white]", console=console) as status:
                        subprocess.run([embedded_python, "-m", "pip", "install", "--no-warn-script-location", "--isolated", "-r", requirements_txt, "--quiet"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            console.print("[bold green]✓[/bold green] Node ecosystem dependencies compiled and locked into embedded runtime.")

        # Step 5: Pull FLUX.2 & FLUX 3 Klein Model Weights, Text Encoders, VAE & Detailer Layers
        console.print("\n[bold magenta]» Allocating FLUX.2 & FLUX 3 Klein Foundational Model Blocks...[/bold magenta]")
        
        # Flux2Klein 9B FP8 Checkpoint
        self.stream_large_file(
            url=self.FLUX2_KLEIN_MODEL_URL,
            dest_path=os.path.join(self.comfy_dir, "models", "checkpoints", "flux-2-klein-9b-fp8.safetensors"),
            description="[bold white]Streaming Flux2Klein 9B FP8 Checkpoint[/bold white]"
        )

        # Flux 2 Text Encoder: qwen_3_8b_fp8mixed.safetensors
        self.stream_large_file(
            url=self.FLUX2_TEXT_ENCODER_URL,
            dest_path=os.path.join(self.comfy_dir, "models", "text_encoders", "qwen_3_8b_fp8mixed.safetensors"),
            description="[bold white]Streaming Qwen 3 8B FP8 Text Encoder[/bold white]"
        )

        # Flux 3 Image Klein INT8 ConvRot Checkpoint
        self.stream_large_file(
            url=self.FLUX3_KLEIN_MODEL_URL,
            dest_path=os.path.join(self.comfy_dir, "models", "checkpoints", "flux3-image-klein-int8-convrot.safetensors"),
            description="[bold white]Streaming Flux3Klein INT8 ConvRot Checkpoint[/bold white]"
        )

        # Flux 3 Image Klein FP8 Text Encoder
        self.stream_large_file(
            url=self.FLUX3_TEXT_ENCODER_URL,
            dest_path=os.path.join(self.comfy_dir, "models", "text_encoders", "flux-3-image-klein-text_encoder-FP8.safetensors"),
            description="[bold white]Streaming Flux3Klein FP8 Text Encoder[/bold white]"
        )

        # Shared FLUX.2 & FLUX 3 VAE: flux2-vae.safetensors
        self.stream_large_file(
            url=self.FLUX2_VAE_URL,
            dest_path=os.path.join(self.comfy_dir, "models", "vae", "flux2-vae.safetensors"),
            description="[bold white]Streaming FLUX.2 & FLUX 3 VAE Layer[/bold white]"
        )
        
        # Edge Tracker: sam_vit_h_4b8939.pth
        self.stream_large_file(
            url=self.SAM_MODEL_URL,
            dest_path=os.path.join(self.comfy_dir, "models", "sams", "sam_vit_h_4b8939.pth"),
            description="[bold white]Streaming Segment Anything (SAM) Model[/bold white]"
        )

        # Ultralytics Face Detector: bbox/face_yolov8n_v2.pt
        self.stream_large_file(
            url=self.FACE_YOLO_URL,
            dest_path=os.path.join(self.comfy_dir, "models", "ultralytics", "bbox", "face_yolov8n_v2.pt"),
            description="[bold white]Streaming Ultralytics Face Detector (YOLOv8n)[/bold white]"
        )

        # Ultralytics Hand Detector: bbox/hand_yolov9c.pt
        self.stream_large_file(
            url=self.HAND_YOLO_URL,
            dest_path=os.path.join(self.comfy_dir, "models", "ultralytics", "bbox", "hand_yolov9c.pt"),
            description="[bold white]Streaming Ultralytics Hand Detector (YOLOv9c)[/bold white]"
        )

        # Ultralytics Foot Detector: bbox/foot_yolov8x_v2.pt
        self.stream_large_file(
            url=self.FOOT_YOLO_URL,
            dest_path=os.path.join(self.comfy_dir, "models", "ultralytics", "bbox", "foot_yolov8x_v2.pt"),
            description="[bold white]Streaming Ultralytics Foot Detector (YOLOv8x)[/bold white]"
        )

        # Step 6: Inject Character Reference Skins & Widescreen Canvases into ComfyUI/input
        console.print("\n[bold magenta]» Provisioning Character Reference Skins & Widescreen Canvases...[/bold magenta]")
        self.inject_comfyui_inputs()

        # Final Status Presentation
        console.print(
            f"\n[bold green]🏁 NON-COMMERCIAL DEMO AUTOMATION PIPELINE ENVIRONMENT PROVISIONED! 🏁[/bold green]\n"
            f"1. Start ComfyUI image-generation [bold cyan]Image-Generation\\ComfyUI_windows_portable\\run_nvidia_gpu.bat[/bold cyan].\n"
            f"2. Drag and drop the Flux2Klein or Flux3Klein Multi-Workflow JSON into the browser window.\n"
            f"3. Toggle [bold cyan]MASTER SWITCH[/bold cyan] between Portrait (1) and Turnaround Sheet (2) then press [bold cyan]Run[/bold cyan].\n"
            f"\n[bold magenta]Powered by Superklok Labs.[/bold magenta]\n"
        )


if __name__ == "__main__":
    try:
        installer = NonCommercialDemoInstaller()
        installer.run()
    except KeyboardInterrupt:
        console.print("\n[bold red]✖ Automation loop terminated by user request.[/bold red]")
        sys.exit(1)

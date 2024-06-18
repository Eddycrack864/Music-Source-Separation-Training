import os
download_dir = "models"
downloads = [
  ("https://huggingface.co/Eddycrack864/Music-Source-Separation-Training/resolve/main/model_bs_roformer_ep_317_sdr_12.9755.ckpt", f"{download_dir}/model_bs_roformer_ep_317_sdr_12.9755.ckpt"),
  ("https://huggingface.co/Eddycrack864/Music-Source-Separation-Training/resolve/main/model_bs_roformer_ep_317_sdr_12.9755.yaml", f"{download_dir}/model_bs_roformer_ep_317_sdr_12.9755.yaml"),
  ("https://huggingface.co/Eddycrack864/Music-Source-Separation-Training/resolve/main/model_bs_roformer_ep_368_sdr_12.9628.ckpt", f"{download_dir}/model_bs_roformer_ep_368_sdr_12.9628.ckpt"),
  ("https://huggingface.co/Eddycrack864/Music-Source-Separation-Training/resolve/main/model_bs_roformer_ep_368_sdr_12.9628.yaml", f"{download_dir}/model_bs_roformer_ep_368_sdr_12.9628.yaml"),
  ("https://huggingface.co/Eddycrack864/Music-Source-Separation-Training/resolve/main/model_bs_roformer_ep_937_sdr_10.5309.ckpt", f"{download_dir}/model_bs_roformer_ep_937_sdr_10.5309.ckpt"),
  ("https://huggingface.co/Eddycrack864/Music-Source-Separation-Training/resolve/main/model_bs_roformer_ep_937_sdr_10.5309.yaml", f"{download_dir}/model_bs_roformer_ep_937_sdr_10.5309.yaml"),
  ("https://huggingface.co/Eddycrack864/Music-Source-Separation-Training/resolve/main/model_mel_band_roformer_ep_3005_sdr_11.4360.ckpt", f"{download_dir}/model_mel_band_roformer_ep_3005_sdr_11.4360.ckpt"),
  ("https://huggingface.co/Eddycrack864/Music-Source-Separation-Training/resolve/main/model_mel_band_roformer_ep_3005_sdr_11.4360.yaml", f"{download_dir}/model_mel_band_roformer_ep_3005_sdr_11.4360.yaml"),
  ("https://huggingface.co/Eddycrack864/Music-Source-Separation-Training/resolve/main/mel_band_roformer_crowd_aufr33_viperx_sdr_8.7144.ckpt", f"{download_dir}/mel_band_roformer_crowd_aufr33_viperx_sdr_8.7144.ckpt"),
  ("https://huggingface.co/Eddycrack864/Music-Source-Separation-Training/resolve/main/model_mel_band_roformer_crowd.yaml", f"{download_dir}/model_mel_band_roformer_crowd.yaml"),
  ("https://huggingface.co/Eddycrack864/Music-Source-Separation-Training/resolve/main/model_bandit_plus_dnr_sdr_11.47.chpt", f"{download_dir}/model_bandit_plus_dnr_sdr_11.47.chpt"),
  ("https://huggingface.co/Eddycrack864/Music-Source-Separation-Training/resolve/main/config_dnr_bandit_bsrnn_multi_mus64.yaml", f"{download_dir}/config_dnr_bandit_bsrnn_multi_mus64.yaml"),
  ("https://huggingface.co/Eddycrack864/Music-Source-Separation-Training/resolve/main/model_vocals_segm_models_sdr_9.77.ckpt", f"{download_dir}/model_vocals_segm_models_sdr_9.77.ckpt"),
  ("https://huggingface.co/Eddycrack864/Music-Source-Separation-Training/resolve/main/config_vocals_segm_models.yaml", f"{download_dir}/config_vocals_segm_models.yaml"),
]
for url, filename in downloads:
    command = f"aria2c -o {filename} {url}"
    os.system(command)

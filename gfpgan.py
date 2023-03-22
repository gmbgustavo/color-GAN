"""
Usage: python inference_gfpgan.py -i inputs/originals -o ./results -v 1.4 -s 2 [options]...

  -h                  show this help
  -i input            Input image or folder. Default: inputs/whole_imgs
  -o output           Output folder. Default: results
  -v version          GFPGAN model version. Option: 1 | 1.2 | 1.3 | 1.4. Default: 1.3
  -s upscale          The final upsampling scale of the image. Default: 2
  -bg_upsampler       background upsampler. Default: realesrgan
  -bg_tile            Tile size for background sampler, 0 for no tile during testing. Default: 400
  -suffix             Suffix of the restored faces
  -only_center_face   Only restore the center face
  -aligned            Input are aligned faces
  -ext                Image extension. Options: auto | jpg | png, auto means using the same ext as inputs. Default: auto

V1.3 Based on V1.2; more natural restoration results; better results on very low-quality / high-quality inputs.
V1.2 No colorization; no CUDA extensions are required. Trained with more data with pre-processing.
V1	 The paper model, with colorization.

python inference_gfpgan.py -i ../originals -o ../results -v 1.4 -s 2 --bg_tile 200


"""


# How to use

## Generate KeyId and Key

Run `main.py` and use the `key_id_hex`, `key_hex` and `iv_hex` with the example shaka packager commands below.

```json
{
 "key_id_guid": "92273ca2-f3b9-4410-928e-8e394f51f007",
 "key_id_hex": "92273ca2f3b94410928e8e394f51f007",
 "key_id_b64": "kic8ovO5RBCSjo45T1HwBw==",
 "key_hex": "859ab314e8e843b97b42bbde16004c60",
 "key_b64": "hZqzFOjoQ7l7QrveFgBMYA==",
 "iv_hex": "611b9b1d1466eb96e8be48d47d65a3fd",
 "iv_b64": "YRubHRRm65bovkjUfWWj/Q==" 
}
```

## Shaka Packager

Run shaka packager with docker and mount your source folder.
```bash
 docker run -v ${PWD}/videos:/media -it --rm google/shaka-packager
```

Package content for Widevine and Playready
```bash
packager \
  skip_encryption=1,in=/media/caminande/audio/audio-caminandes_audio_aac_128k.mp4,stream=audio,output=/media/output/dash/audio.mp4 \
  in=/media/caminande/video/HD-caminandes_h264_high_1080p_6000.mp4,stream=video,output=/media/output/dash/video.mp4,drm_label=HD \
  --enable_raw_key_encryption \
  --keys label=HD:key_id=4a6078e2a0c64b52a5e7a310981c835f:key=1a48eb3e55f3b965052d51ea00ac6ace \
  --protection_systems Widevine,PlayReady \
  --mpd_output /media/output/dash/content.mpd
```

Package content for Fairplay
```bash
packager \
  skip_encryption=1,in=/media/caminande/audio/audio-caminandes_audio_aac_128k.mp4,stream=audio,output=/media/output/hls/audio.mp4 \
  in=/media/caminande/video/HD-caminandes_h264_high_1080p_6000.mp4,stream=video,output=/media/output/hls/video.mp4,drm_label=HD \
  --protection_scheme cbcs \
  --enable_raw_key_encryption \
  --keys label=HD:key_id=92273ca2f3b94410928e8e394f51f007:key=859ab314e8e843b97b42bbde16004c60 \
  --protection_systems FairPlay \
  --iv 611b9b1d1466eb96e8be48d47d65a3fd \
  --hls_master_playlist_output /media/output/hls/h264_master.m3u8 \
  --hls_key_uri skd://testAssetID
```

## Host Files
In the `/server` folder, build image for nginx
```bash
 docker build -t barb/simple-server .
 ```

From the root of the project run image with mounting the ouput folder
```bash
docker run -d -v ${PWD}/videos/output:/var/www -p 8090:80 barb/simple-server
```

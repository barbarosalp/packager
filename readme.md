# How to use

## Shaka Packager

Run shaka packager with docker and mount your source folder.
```bash
 docker run -v ${PWD}/videos:/media -it --rm google/shaka-packager
```

Package content
```bash
packager \
  skip_encryption=1,in=/media/caminandes/audio/audio-caminandes_audio_aac_128k.mp4,stream=audio,output=/media/output/audio.mp4 \
  in=/media/caminandes/video/HD-caminandes_h264_high_1080p_6000.mp4,stream=video,output=/media/output/video.mp4,drm_label=HD \
  --enable_raw_key_encryption \
  --keys label=HD:key_id=4a6078e2a0c64b52a5e7a310981c835f:key=1a48eb3e55f3b965052d51ea00ac6ace \
  --protection_systems Widevine,PlayReady \
  --mpd_output /media/output/content.mpd
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

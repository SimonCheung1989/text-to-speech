#!/bin/sh

ls -F output/audio | grep .wav | awk -F ".wav" '{print $1}' | xargs -I {} ffmpeg -i output/audio/{}.wav -acodec mp3 output/audio/{}.mp3

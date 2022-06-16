from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip

import cv2
import os

class Video:
    def __init__(self, audio_file, image_file):
        self.image_frame = cv2.imread(image_file)
        self.audio_clip = AudioFileClip(audio_file).volumex(1.0)
        self.audio_duration = self.audio_clip.duration
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')

        
    def build_video(self):
        height, width, layers = self.image_frame.shape
        video = cv2.VideoWriter('output/temp_video.avi', self.fourcc, 1.0, (width, height))
        for _ in range(round(self.audio_duration)):
            video.write(self.image_frame)
        
        
        cv2.destroyAllWindows()
        video.release()
        final_video = VideoFileClip('output/temp_video.avi')
        audio_subclip = self.audio_clip.subclip(0, self.audio_duration)
        final_video = final_video.set_audio(audio_subclip)
        final_video.write_videofile("output/final.mp4")


video = Video('audio/vmachucar.mp3', 'images/eu.jpeg')

video.build_video()

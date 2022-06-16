from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip

import cv2
import os

class Video:
    def __init__(self, audio_file, image_file):
        self.image_frame = cv2.imread(image_file)
        self.audio_clip = AudioFileClip(audio_file).volumex(1.0)
        self.audio_duration = self.audio_clip.duration
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')

        # self.video_file = video_file
        # self.video_clip = VideoFileClip(video_file)
        # self.video_duration = self.video_clip.duration
        
    def build_video(self):
        height, width, layers = self.image_frame.shape
        video = cv2.VideoWriter('output.avi', self.fourcc, 1.0, (width, height))
        for _ in range(round(self.audio_duration)):
            video.write(self.image_frame)
        
        
        cv2.destroyAllWindows()
        video.release()
        final_video = VideoFileClip('./output.avi')
        audio_subclip = self.audio_clip.subclip(0, self.audio_duration)
        final_video = final_video.set_audio(audio_subclip)
        final_video.write_videofile("final.mp4")

    def merge_audio_video(self):
        pass
        # self.audio_clip.audio_fadein(0.5).audio_fadeout(0.5)

video = Video('./audio/Mtg Vou Machucar.mp3', './images/mf_aviles_midea.jpeg')

video.build_video()

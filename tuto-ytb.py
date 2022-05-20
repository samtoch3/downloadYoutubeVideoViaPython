# -*- coding: utf-8 -*-
"""
Created on Wed May 18 23:09:25 2022

@author: Samson Thibaut
"""
from pytube import YouTube

link ='https://www.youtube.com/watch?v=vU-P-K5qtDM'

video = YouTube(link)

video.streams.filter(res='720p').first().download()
#!/usr/bin/env python
"""Class to undertaken audio feature analysis"""

from featureextractor import ConstQSegmentExtractor, LoudnessExtractor, ApplauseExtractor
from audiodata import AudioData

class AudioAnalyser(object):
    def __init__(self, config):
        self.windowSize = config['WindowSize']
        self.loaded = False
        self.features = {ConstQSegmentExtractor(),
                         LoudnessExtractor(),
                         ApplauseExtractor()}
        self.audio = AudioData()

    def loadAudio(self, fileName):
        self.audio.loadFile(fileName)
        self.loaded = True

    def processAll(self):
        for featureExtractor in self.features:
            featureExtractor.processRemaining()
        """Process all audio according to feature extractor plugins
        """

    def processFrames(self):
        for frame in self.audio.frames(self.windowSize):
            for featureExtractor in self.features:
                featureExtractor.process(frame)



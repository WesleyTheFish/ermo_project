from collections import deque

class Pipeline:
    def __init__(self, transform_funcs):
        self.transform_funcs = transform_funcs

    def run_pipeline(self, sample):
        for transform_func in self.transform_funcs:
            sample = transform_func(sample)
        return sample
    
# range is distance from center
def make_deadzone_transform(center, range):
    def function(sample):
        if center - range <= sample <= center + range:
            return center
        return sample
    return function

def make_expo_transform(expo):
    def function(sample):
        return sample
    return function

def make_window_filter_transform(width):
    dq = deque(maxlen=width)
    def function(sample):
        dq.append(sample)
        return sum(dq)/len(dq)
    return function
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

class Transform:
    """Transform base class"""
    def __call__(self, sample):
        """
        Transform the sample.
        The __call__ method should be overridden by subclasses to allow function like behavior.
        
        xform = Transform()
        transformed_sample = xform(sample)

        Class instances can be used exactly like functions using closures.

        Args:
            sample: The input sample to transform.
        Returns:
            The transformed sample.
        """
        return sample

class WindowTransform(Transform):
    """Class based window transform showing same behavior as the function based version."""
    def __init__(self, width):

        self.dq = deque(maxlen=width)

    def __call__(self, sample):
        """
        Apply a window filter to the sample.
        This method appends the sample to a deque and returns the average of the samples in the
        deque.
        
        Example usage:
        wxf = WindowTransform(width=5)
        transformed_sample = wxf(sample)

        """
        self.dq.append(sample)
        return sum(self.dq) / len(self.dq)
from chainer import cuda

def float_to_cpu(x):
    return float(cuda.to_cpu(x.data))

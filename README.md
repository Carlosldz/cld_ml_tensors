# module_structure

This module has two main objects, a TensorBuilder class and a TensorCalculator class, made to work with 2D tensors. The reason why it's divided into two is so that they can be further expanded while retaining a specific functionality. Neither of these has a fleshed out constructor in order to make this module work similarly to other popular modules such as numpy and pandas. This means that you will only need one instance of the classes active at any time, but you'll need to input the arguments on every call.

TensorBuilder is initially made of three methods:
- Allzeros
- Allones
- Allrand
  All three of these take in a tuple of two integers as the size of the output tensor, which is made of all zeros, ones, or random numbers from [0,1], respectively.

TensorCalculator is made of several more methods, among which stand:
- Tensorsum, takes in two tensors and attemps to add them up. If they're not of compatible size (aka. equal size), it raises an error.
- Tensormult, takes in two tensors and attempts to multiply them. It'll first try to multiply the first with the second, and if it fails, it attemps it the other way around. In case both fail, it raises an error.
- Sumreshape, takes in two tensors and attempts to reshape the first tensor to match the second one. However, not all tensor sizes are compatible with the reshape function, so it may raise an error.
- Multreshape, takes in two tensors and attempts to reshape the first tensor to be the transposed of the second one. However, it may also fail due to incompatibility.
- Tensorlog, takes one tensor and performs the natural logarithm.
- Tensorsqrt, takes one tensor and performs the square root on the absolute value of all values of the tensor.

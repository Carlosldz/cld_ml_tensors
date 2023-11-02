# coding: utf-8

import torch

"""
This module is designed around 2D tensors, as per the assignment's instructions
"""

__all__ = ["TensorCalculator", "TensorBuilder"]


class TensorBuilder():

    def __init__(self):
        return None

    
    @staticmethod
    def allzeros(size: (int, int)):
        return torch.zeros(size)
    
    @staticmethod
    def allones(size: (int, int)):
        return torch.ones(size)
    
    @staticmethod
    def allrand(size: (int, int)):
        return torch.rand(size)


class TensorCalculator():

    def __init__(self):
        return None
    
    @staticmethod
    def tensorsum(tensor1, tensor2):
        try:
            return torch.add(tensor1, tensor2)
        except:
            raise RuntimeError("The tensors are not of equal size. Try using the method 'sumreshape' first")
    
    @staticmethod
    def tensormult(tensor1, tensor2):
        """
        tensormult will first try to multiply the first tensor with the second one, but if it's unable to, it'll 
        first try to swap the order (multiply the second tensor with the first one) before raising and error
        """
        if tensor1.size()[1] == tensor2.size()[0]:
            return torch.matmul(tensor1, tensor2)
        elif tensor1.size()[0] == tensor2.size()[1]:
            return torch.matmul(tensor2, tensor1)
        else:
            raise RuntimeError("Neither tensor has matching sizes, so it is suggested you execute the "
                               "'multreshape' function.")
    
    @staticmethod
    def sumreshape(tensor1, tensor2):
        """
        sumreshape is a function that adjusts tensor1's size to tensor2's, so long as they have compatible shapes,
        in order to sum them up
        """
        try:
            return tensor1.reshape_as(tensor2)
        except:
            raise RuntimeError("The tensors have non-compatible shapes")
            
    
    @staticmethod
    def multreshape(tensor1, tensor2):
        """
        multreshape is a function that adjusts tensor1's size to tensor2's, so long as they have compatible shapes,
        in order to multiply them
        """
        try:
            return tensor1.reshape_as(tensor2).transpose(0,1)
        except:
            raise RuntimeError("The tensors have non-compatible shapes")
    
    @staticmethod
    def tensorlog(tensor1):
        return torch.log(tensor1)
    
    @staticmethod
    def tensorsqrt(tensor1):
        """
        Returns the square root of the given tensor, except any values that were previously negative, are first turned
        positive.
        """
        tensor = tensor1.abs().sqrt()
        return tensor
        


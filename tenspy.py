class tenspy:

    def __init__(self, ten):

        self.ten = ten

        self.__pri = 1

        self.dtype = "dtype = tenspy"

    def ones(self, t):
        '''
        returns a tensor of 1's with the specified shape.

        :param t: tuple of tensor shape
        :return: tensor of 1's
        '''

        l = len(t)
        self.ten = 1
        return _tenspy__build_ones(self.ten, l - 1, t)



    def __build_ones(self, inp, j, t):
        '''
        recursive functions called for every dimension i.e. len(shape tuple)
        in which computed output tensor is sent as input and its reused for further computation.

        :param inp: tensor of 1's
        :param j: dimension counter
        :param t: shape tuple
        :return: computed tensor
        '''
        if j < 0:
            return inp

        out = []
        for i in range(t[j]):
            out.append(inp)

        return build_ones(out, j - 1, t)

    def reshape(self, t):
        '''
        The input tensor is converted into a 1 dimensional tensor (i.e. 1D python list)
        and the 1D tensor is reshaped as per the input shape tuple parameter.

        :param inp: input tensor
        :param t: tuple of desired output shape
        :return: reshaped tensor as per input provided shape tuple
        '''
        out_list, out_reshaped = [], []

        _tenspy__build_list(self.ten, out_list)

        # print('list', out_list)

        order = 1
        for t1 in t:
            order *= t1

        assert len(out_list) == order, 'reshaping not possible due to tensor size mismatch'

        return _tenspy__reshape_tensor_from_list(out_list, t)

    def __build_list(inp, out):
        '''

        :param inp: input tensor
        :param out: empty tensor being reshaped as 1D tensor in this function.
        '''
        for j in inp:
            if type(j) is list:
                build_list(j, out)
            else:
                out.append(j)

    def __reshape_tensor_from_list(inp, t, j=0, ci=[0]):
        '''
        recursive function which creates a tensor as per the shape specified.

        :param inp: 1D tensor
        :param t: shape tuple
        :param j: dimension counter used to stop recursive calls
        :param ci: index for 1D tensor
        :return: reshaped tensor
        '''
        out = []
        for i in range(t[j]):
            if j < len(t) - 1:
                out.append(reshape_tensor_from_list(inp, t, j + 1, ci))
            else:
                out.append(inp[ci[0]])
                ci[0] += 1

        del inp
        return out




def ones(t):
    '''
    returns a tensor of 1's with the specified shape.

    :param t: tuple of tensor shape
    :return: tensor of 1's
    '''

    l = len(t)
    inp = 1
    return build_ones(inp, l - 1, t)


def build_ones(inp, j, t):
    '''
    recursive functions called for every dimension i.e. len(shape tuple)
    in which computed output tensor is sent as input and its reused for further computation.

    :param inp: tensor of 1's
    :param j: dimension counter
    :param t: shape tuple
    :return: computed tensor
    '''
    if j < 0:
        return inp

    out = []
    for i in range(t[j]):
        out.append(inp)

    return build_ones(out, j - 1, t)


def reshape(inp, t):
    '''
    The input tensor is converted into a 1 dimensional tensor (i.e. 1D python list)
    and the 1D tensor is reshaped as per the input shape tuple parameter.

    :param inp: input tensor
    :param t: tuple of desired output shape
    :return: reshaped tensor as per input provided shape tuple
    '''
    out_list, out_reshaped = [], []

    build_list(inp, out_list)

    # print('list', out_list)

    order = 1
    for t1 in t:
        order *= t1

    assert len(out_list) == order, 'reshaping not possible due to tensor size mismatch'

    return reshape_tensor_from_list(out_list, t)



def build_list(inp, out):
    '''

    :param inp: input tensor
    :param out: empty tensor being reshaped as 1D tensor in this function.
    '''
    for j in inp:
        if type(j) is list:
            build_list(j, out)
        else:
            out.append(j)


def reshape_tensor_from_list(inp, t, j=0, ci=[0]):
    '''
    recursive function which creates a tensor as per the shape specified.

    :param inp: 1D tensor
    :param t: shape tuple
    :param j: dimension counter used to stop recursive calls
    :param ci: index for 1D tensor
    :return: reshaped tensor
    '''
    out = []
    for i in range(t[j]):
        if j < len(t) - 1:
            out.append(reshape_tensor_from_list(inp, t, j + 1, ci))
        else:
            out.append(inp[ci[0]])
            ci[0] += 1

    del inp
    return out

#def dot(inp1, inp2):





# on = ones((2, 4, 4))
# print(on)
#
# print(reshape(on, (2, 2, 8)))
#
# print(ones((1, 1, 1, 1, 1, 1)))
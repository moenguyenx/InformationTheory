import math

class Compress:
    # Compress class for storing different parameters of a character
    def __init__(self, char):
        self.original = char
        self.count = 0
        self.code = ""
        self.probability = 0


class ShannonFanoCompression:
    # Shannon Compression Class for compressing data using Shannon-Fano encoding

    def get_probability(self, compressor):
        return compressor.probability

    def compress_data(self, data):
        '''
        Compress data using Shannon-Fano encoding.
        1. Process the input string and find the probability of each unique character.
        2. Sort characters based on probability in descending order.
        3. Split characters into two groups recursively until each group has only one character.
        4. Assign '0' to the first group and '1' to the second group.
        5. Return the sorted compressor list.

        Args:
        - data (str): Input string to be compressed.

        Returns:
        - list: Sorted list of Compress objects.
        '''
        processed = []
        compressor = []
        total_length = len(data)

        for i in range(len(data)):
            if data[i] not in processed:
                processed.append(data[i])
                count = data.count(data[i])
                probability = count / total_length
                comp = Compress(data[i])
                comp.count = count
                comp.probability = probability
                compressor.append(comp)

        sorted_compressor = sorted(
            compressor, key=self.get_probability, reverse=True)
        self._encoder(sorted_compressor)
        return sorted_compressor

    def _encoder(self, compressor):
        '''
        Helper function for encoding characters with Shannon-Fano algorithm.

        Args:
        - compressor (list): List of Compress objects.

        Returns:
        - None
        '''
        if len(compressor) > 1:
            split = self._splitter(
                probability=[i.probability for i in compressor], pointer=0)
            part_1 = compressor[:split + 1]
            for i in part_1:
                i.code += '0'
            self._encoder(part_1)
            part_2 = compressor[split + 1:]
            for i in part_2:
                i.code += '1'
            self._encoder(part_2)

    def _splitter(self, probability, pointer):
        '''
        Helper function for splitting probabilities in Shannon-Fano algorithm.

        Args:
        - probability (list): List of probabilities.
        - pointer (int): Current position in the probability list.

        Returns:
        - int: Splitting point index.
        '''
        diff = sum(probability[:pointer + 1]) - \
            sum(probability[pointer + 1:])
        if diff < 0:
            point = self._splitter(probability, pointer + 1)
            diff_1 = sum(probability[:point]) - sum(probability[point:])
            diff_2 = sum(probability[:point + 1]) - sum(probability[point + 1:])
            if abs(diff_1) < abs(diff_2):
                return point - 1
            return point
        else:
            return pointer


# Main Function
def shannon_fano_main_func():
     # Get input from the user
    user_input = input("Enter the data to be compressed: ")
    
    # Create an instance of ShannonFanoCompression
    compressor = ShannonFanoCompression()

    # Compress the user input
    compressed_data = compressor.compress_data(user_input)
    entropy = 0

    for i in compressed_data:
        entropy -= i.probability* math.log2(i.probability)
    print(f"Entropy: {entropy}")

    # Display the compressed data
    for i in compressed_data:
        print(f"Character-- {i.original}:: Code-- {i.code} :: Probability-- {i.probability}")




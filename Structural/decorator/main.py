from Structural.decorator.cloud_stream import CloudStream
from Structural.decorator.compressed_cloud_stream import CompressedCloudStream
from Structural.decorator.encripted import Encrypted
from Structural.decorator.stream import Stream


class CreditCard:

    @staticmethod
    def store_credit_card(stream: Stream):
        stream.write("1234-4567-2345-9876")


if __name__ == '__main__':
    CreditCard.store_credit_card(CompressedCloudStream(CloudStream()))
    CreditCard.store_credit_card(Encrypted(CloudStream()))


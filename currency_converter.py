"""
You are given the following parameters:
Rates: ['USD', 'JPY', 110] ['US', 'AUD', 1.45] ['JPY', 'GBP', 0.0070]
To/From currency ['GBP', 'AUD']
"""

from typing import List


class CurrencyConverter():
    def __init__(self, rates):
        # ['USD', 'JPY', 110] ['US', 'AUD', 1.45] ['JPY', 'GBP', 0.0070]
        # TBD: Create the internal data layer.
        self._data = {} # {'USD':[['JPY', 110], ['AUD', 1.45]}
        for rate in rates:
            src, dst, x = rate[0], rate[1], rate[2]
            if src not in self._data:
                self._data[src] = []
            self._data[src].append([dst, x])
            # For simplicity - Backwards link
            if dst not in self._data:
                self._data[dst] = []
            self._data[dst].append([src, 1/x])


    def convert(self, from_currency, to_currency, exclude=[]):
        """
        Algo: TBD
        """
        print('{}->{} Exclude: {}'.format(from_currency, to_currency, exclude))
        if from_currency not in self._data or to_currency not in self._data:
            print("Currencies not supporty")
            return None
        else:
            if from_currency == to_currency:
                return 1
            else:
                for dst_currency_data in self._data.get(from_currency):
                    dst_currency, x = dst_currency_data[0], dst_currency_data[1]
                    if dst_currency not in exclude:
                        exclude.append(from_currency)
                        ret = x * self.convert(dst_currency, to_currency, exclude=exclude)
                        if ret is None:
                            continue
                        else:
                            return ret
                return None

if __name__ == "__main__":
    CC = CurrencyConverter([['USD', 'JPY', 110],
                            ['USD', 'AUD', 1.45],
                            ['JPY', 'GBP', 0.0070]
                           ])
    print(CC._data)
    print(CC.convert('GBP', 'AUD'))


"""
Output:
python3 currency.py 
{'USD': [['JPY', 110], ['AUD', 1.45]], 'JPY': [['USD', 0.00909090909090909], ['GBP', 0.007]], 'AUD': [['USD', 0.6896551724137931]], 'GBP': [['JPY', 142.85714285714286]]}
GBP->AUD Exclude: []
JPY->AUD Exclude: ['GBP']
USD->AUD Exclude: ['GBP', 'JPY']
AUD->AUD Exclude: ['GBP', 'JPY', 'USD']
1.883116883116883

"""

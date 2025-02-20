# poker_isomorphisms
 
poker_isomorphisms is a Python library for dealing with flop isomorphisms in relation to poker.
Isomorphic in poker refers to strategically equivalent cards. Isomorphic hands can apply to hole cards or community cards (aka a flop). There are 22100 possible flops out of which 1755 are strategically different.

Example 1) AsKs is strategically identical to AcKc on a Th9h7h flop; therefore, these two hands are isomorphic.
Example 2) Kh9s3h is strategically identical to Kd9c3d; therefore, these two flops are isomorphic.

[GTO Wizard](https://gtowizard.com/glossary/isomorphic/)

[PioSOLVER](https://piosolver.com/blog/2015-11-05-flop-subsets/)

## Links

Documentation: 

Code: https://github.com/Thurpan/poker_isomorphisms

Pip: https://pypi.org/project/poker_isomorphisms/

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install poker_isomorphisms.

```bash
pip install poker_isomorphisms
```

## Usage

```python
import poker_isomorphisms

poker_isomorphisms.flop_isomorphisms('2dAd2s')
# returns ['As2s2h', 'As2h2s', '2sAs2h', '2s2hAs', '2hAs2s', '2h2sAs', 'As2s2d', 'As2d2s', '2sAs2d', '2s2dAs', '2dAs2s', '2d2sAs', 'As2s2c', 'As2c2s', '2sAs2c', '2s2cAs', '2cAs2s', '2c2sAs', 'Ah2h2s', 'Ah2s2h', '2hAh2s', '2h2sAh', '2sAh2h', '2s2hAh', 'Ah2h2d', 'Ah2d2h', '2hAh2d', '2h2dAh', '2dAh2h', '2d2hAh', 'Ah2h2c', 'Ah2c2h', '2hAh2c', '2h2cAh', '2cAh2h', '2c2hAh', 'Ad2d2s', 'Ad2s2d', '2dAd2s', '2d2sAd', '2sAd2d', '2s2dAd', 'Ad2d2h', 'Ad2h2d', '2dAd2h', '2d2hAd', '2hAd2d', '2h2dAd', 'Ad2d2c', 'Ad2c2d', '2dAd2c', '2d2cAd', '2cAd2d', '2c2dAd', 'Ac2c2s', 'Ac2s2c', '2cAc2s', '2c2sAc', '2sAc2c', '2s2cAc', 'Ac2c2h', 'Ac2h2c', '2cAc2h', '2c2hAc', '2hAc2c', '2h2cAc', 'Ac2c2d', 'Ac2d2c', '2cAc2d', '2c2dAc', '2dAc2c', '2d2cAc']

poker_isomorphisms.flop_normalise('7cQc3s')
# returns "Qs7s3h"
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Authors

* Euan McNicholas [GitHub](https://github.com/Thurpan)
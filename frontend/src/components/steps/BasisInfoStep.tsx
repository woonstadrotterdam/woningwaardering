import React from 'react';
import { FormData } from '../../types';

interface Props {
  formData: FormData;
  updateFormData: (updates: Partial<FormData>) => void;
}

const BasisInfoStep: React.FC<Props> = ({ formData, updateFormData }) => {
  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold text-gray-800 mb-4">Basis Informatie</h2>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Woning ID
        </label>
        <input
          type="text"
          value={formData.id || ''}
          onChange={(e) => updateFormData({ id: e.target.value })}
          className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
          placeholder="Bijvoorbeeld: WONING-001"
        />
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Bouwjaar
        </label>
        <input
          type="number"
          value={formData.bouwjaar || ''}
          onChange={(e) => updateFormData({ bouwjaar: parseInt(e.target.value) || undefined })}
          className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
          placeholder="Bijvoorbeeld: 1990"
          min="1800"
          max={new Date().getFullYear()}
        />
      </div>

      <div className="border-t pt-4">
        <h3 className="text-lg font-semibold text-gray-800 mb-4">Adresgegevens</h3>

        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Straatnaam
            </label>
            <input
              type="text"
              value={formData.adres?.straatnaam || ''}
              onChange={(e) =>
                updateFormData({
                  adres: { ...formData.adres, straatnaam: e.target.value },
                })
              }
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
              placeholder="Bijvoorbeeld: Hoofdstraat"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Huisnummer
            </label>
            <input
              type="text"
              value={formData.adres?.huisnummer || ''}
              onChange={(e) =>
                updateFormData({
                  adres: { ...formData.adres, huisnummer: e.target.value },
                })
              }
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
              placeholder="Bijvoorbeeld: 123"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Postcode
            </label>
            <input
              type="text"
              value={formData.adres?.postcode || ''}
              onChange={(e) =>
                updateFormData({
                  adres: { ...formData.adres, postcode: e.target.value },
                })
              }
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
              placeholder="Bijvoorbeeld: 1234AB"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Toevoeging (optioneel)
            </label>
            <input
              type="text"
              value={formData.adres?.huisnummerToevoeging || ''}
              onChange={(e) =>
                updateFormData({
                  adres: { ...formData.adres, huisnummerToevoeging: e.target.value },
                })
              }
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
              placeholder="Bijvoorbeeld: A"
            />
          </div>
        </div>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          BAG Identificatie (optioneel)
        </label>
        <input
          type="text"
          value={formData.adresseerbaarObjectBasisregistratie?.bagIdentificatie || ''}
          onChange={(e) =>
            updateFormData({
              adresseerbaarObjectBasisregistratie: {
                bagIdentificatie: e.target.value,
              },
            })
          }
          className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
          placeholder="Bijvoorbeeld: 0344010000000001"
        />
        <p className="text-sm text-gray-500 mt-1">
          BAG ID is nodig voor controle of het een rijksmonument is
        </p>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Peildatum (optioneel)
        </label>
        <input
          type="date"
          value={formData.peildatum || ''}
          onChange={(e) => updateFormData({ peildatum: e.target.value })}
          className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
        />
        <p className="text-sm text-gray-500 mt-1">
          Datum waarop de berekening plaatsvindt (standaard: vandaag)
        </p>
      </div>
    </div>
  );
};

export default BasisInfoStep;

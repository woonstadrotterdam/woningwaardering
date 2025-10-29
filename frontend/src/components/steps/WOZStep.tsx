import React from 'react';
import { FormData, WOZEenheid } from '../../types';

interface Props {
  formData: FormData;
  updateFormData: (updates: Partial<FormData>) => void;
}

const WOZStep: React.FC<Props> = ({ formData, updateFormData }) => {
  const updateWOZ = (updates: Partial<WOZEenheid>) => {
    const currentWOZ = formData.wozEenheden?.[0] || { vastgesteldeWaarde: 0, waardepeildatum: '' };
    updateFormData({
      wozEenheden: [{ ...currentWOZ, ...updates }],
    });
  };

  const currentWOZ = formData.wozEenheden?.[0];

  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold text-gray-800 mb-4">WOZ Waarde</h2>

      <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 mb-6">
        <p className="text-sm text-blue-800">
          De WOZ-waarde (Wet Waardering Onroerende Zaken) bepaalt een deel van de
          woningwaardering punten. Hoe hoger de WOZ-waarde, hoe meer punten de woning krijgt.
        </p>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          WOZ Waarde (€)
        </label>
        <input
          type="number"
          step="1000"
          value={currentWOZ?.vastgesteldeWaarde || ''}
          onChange={(e) =>
            updateWOZ({ vastgesteldeWaarde: parseFloat(e.target.value) || 0 })
          }
          className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
          placeholder="Bijvoorbeeld: 250000"
          min="0"
        />
        <p className="text-sm text-gray-500 mt-1">
          De vastgestelde WOZ-waarde van de woning in euro's
        </p>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Waardepeildatum
        </label>
        <input
          type="date"
          value={currentWOZ?.waardepeildatum || ''}
          onChange={(e) => updateWOZ({ waardepeildatum: e.target.value })}
          className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
        />
        <p className="text-sm text-gray-500 mt-1">
          De datum waarop de WOZ-waarde is vastgesteld (staat op de WOZ-beschikking)
        </p>
      </div>

      <div className="bg-green-50 border border-green-200 rounded-lg p-4">
        <h4 className="font-semibold text-green-800 mb-2">Waar vind ik mijn WOZ-waarde?</h4>
        <ul className="text-sm text-green-800 list-disc list-inside space-y-1">
          <li>Op de jaarlijkse WOZ-beschikking van de gemeente</li>
          <li>Via MijnOverheid.nl onder 'Berichten'</li>
          <li>Door contact op te nemen met de gemeente</li>
        </ul>
      </div>

      {currentWOZ && currentWOZ.vastgesteldeWaarde > 0 && (
        <div className="bg-gray-50 border border-gray-300 rounded-lg p-4">
          <h4 className="font-semibold text-gray-800 mb-2">Samenvatting</h4>
          <div className="space-y-1 text-sm text-gray-700">
            <p>
              <strong>WOZ-waarde:</strong> €{' '}
              {currentWOZ.vastgesteldeWaarde.toLocaleString('nl-NL')}
            </p>
            {currentWOZ.waardepeildatum && (
              <p>
                <strong>Peildatum:</strong>{' '}
                {new Date(currentWOZ.waardepeildatum).toLocaleDateString('nl-NL')}
              </p>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default WOZStep;

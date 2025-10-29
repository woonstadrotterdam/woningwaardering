import React from 'react';
import { FormData, Energieprestatie } from '../../types';

interface Props {
  formData: FormData;
  updateFormData: (updates: Partial<FormData>) => void;
}

const EnergieprestatieStep: React.FC<Props> = ({ formData, updateFormData }) => {
  const energielabels = [
    'A+++++',
    'A++++',
    'A+++',
    'A++',
    'A+',
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
  ];

  const updateEnergieprestatie = (updates: Partial<Energieprestatie>) => {
    const currentEP = formData.energieprestaties?.[0] || {};
    updateFormData({
      energieprestaties: [{ ...currentEP, ...updates }],
    });
  };

  const currentEP = formData.energieprestaties?.[0];

  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold text-gray-800 mb-4">Energieprestatie</h2>

      <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 mb-6">
        <p className="text-sm text-blue-800">
          De energieprestatie kan punten opleveren of kosten. Een goed energielabel (A+ of
          hoger) levert punten op, een slecht label (E, F, G) kost punten.
        </p>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Energielabel
        </label>
        <select
          value={currentEP?.label || ''}
          onChange={(e) => updateEnergieprestatie({ label: e.target.value || undefined })}
          className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
        >
          <option value="">-- Selecteer energielabel --</option>
          {energielabels.map((label) => (
            <option key={label} value={label}>
              {label}
            </option>
          ))}
        </select>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Type Energieprestatie
        </label>
        <select
          value={currentEP?.soort?.code || ''}
          onChange={(e) =>
            updateEnergieprestatie({
              soort: e.target.value ? { code: e.target.value } : undefined,
            })
          }
          className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
        >
          <option value="">-- Selecteer type --</option>
          <option value="EP1">EP1 - Energieprestatie-index</option>
          <option value="EP2">EP2 - Energie-Index</option>
          <option value="EP3">EP3 - BENg (Bijna Energieneutrale Gebouwen)</option>
        </select>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Energieprestatie Waarde (optioneel)
        </label>
        <input
          type="number"
          step="0.01"
          value={currentEP?.waarde || ''}
          onChange={(e) =>
            updateEnergieprestatie({ waarde: parseFloat(e.target.value) || undefined })
          }
          className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
          placeholder="Bijvoorbeeld: 1.25"
        />
        <p className="text-sm text-gray-500 mt-1">
          Numerieke waarde van de energieprestatie (indien beschikbaar)
        </p>
      </div>

      <div className="grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Begindatum
          </label>
          <input
            type="date"
            value={currentEP?.begindatum || ''}
            onChange={(e) => updateEnergieprestatie({ begindatum: e.target.value })}
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Einddatum (optioneel)
          </label>
          <input
            type="date"
            value={currentEP?.einddatum || ''}
            onChange={(e) => updateEnergieprestatie({ einddatum: e.target.value })}
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
          />
        </div>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Status
        </label>
        <select
          value={currentEP?.status?.code || 'DEF'}
          onChange={(e) =>
            updateEnergieprestatie({
              status: { code: e.target.value },
            })
          }
          className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
        >
          <option value="DEF">Definitief</option>
          <option value="VOR">Voorlopig</option>
        </select>
      </div>

      <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-4">
        <p className="text-sm text-yellow-800">
          <strong>Let op:</strong> Voor een geldige berekening is minimaal het energielabel
          vereist. De andere velden zijn optioneel maar kunnen de berekening verfijnen.
        </p>
      </div>
    </div>
  );
};

export default EnergieprestatieStep;

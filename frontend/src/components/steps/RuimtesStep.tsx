import React, { useState } from 'react';
import { FormData, Ruimte } from '../../types';
import { FaPlus, FaTrash } from 'react-icons/fa';

interface Props {
  formData: FormData;
  updateFormData: (updates: Partial<FormData>) => void;
}

const RuimtesStep: React.FC<Props> = ({ formData, updateFormData }) => {
  const [editingIndex, setEditingIndex] = useState<number | null>(null);

  const addRuimte = () => {
    const newRuimte: Ruimte = {
      id: `RUIMTE-${Date.now()}`,
      naam: '',
      soort: { code: 'VTK' },
      oppervlakte: 0,
      verwarmd: true,
    };

    updateFormData({
      ruimten: [...(formData.ruimten || []), newRuimte],
    });
    setEditingIndex((formData.ruimten || []).length);
  };

  const updateRuimte = (index: number, updates: Partial<Ruimte>) => {
    const updatedRuimten = [...(formData.ruimten || [])];
    updatedRuimten[index] = { ...updatedRuimten[index], ...updates };
    updateFormData({ ruimten: updatedRuimten });
  };

  const deleteRuimte = (index: number) => {
    const updatedRuimten = (formData.ruimten || []).filter((_, i) => i !== index);
    updateFormData({ ruimten: updatedRuimten });
    if (editingIndex === index) {
      setEditingIndex(null);
    }
  };

  const ruimteTypes = {
    VTK: [
      { code: 'WOO', name: 'Woonkamer' },
      { code: 'SLA', name: 'Slaapkamer' },
      { code: 'KEU', name: 'Keuken' },
      { code: 'BAD', name: 'Badkamer' },
    ],
    OVR: [
      { code: 'BER', name: 'Berging' },
      { code: 'ZOL', name: 'Zolder' },
      { code: 'KEL', name: 'Kelder' },
      { code: 'GAR', name: 'Garage' },
    ],
  };

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold text-gray-800">Ruimtes</h2>
        <button
          onClick={addRuimte}
          className="flex items-center gap-2 px-4 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700"
        >
          <FaPlus /> Ruimte Toevoegen
        </button>
      </div>

      {!formData.ruimten || formData.ruimten.length === 0 ? (
        <div className="text-center py-8 text-gray-500">
          Nog geen ruimtes toegevoegd. Klik op "Ruimte Toevoegen" om te beginnen.
        </div>
      ) : (
        <div className="space-y-4">
          {formData.ruimten.map((ruimte, index) => (
            <div
              key={ruimte.id}
              className="border border-gray-300 rounded-lg p-4 bg-gray-50"
            >
              <div className="flex justify-between items-start mb-4">
                <h3 className="text-lg font-semibold text-gray-800">
                  Ruimte {index + 1}
                  {ruimte.naam && `: ${ruimte.naam}`}
                </h3>
                <button
                  onClick={() => deleteRuimte(index)}
                  className="text-red-600 hover:text-red-800"
                >
                  <FaTrash />
                </button>
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Naam
                  </label>
                  <input
                    type="text"
                    value={ruimte.naam}
                    onChange={(e) => updateRuimte(index, { naam: e.target.value })}
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500"
                    placeholder="Bijvoorbeeld: Woonkamer"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Oppervlakte (m²)
                  </label>
                  <input
                    type="number"
                    step="0.01"
                    value={ruimte.oppervlakte}
                    onChange={(e) =>
                      updateRuimte(index, { oppervlakte: parseFloat(e.target.value) || 0 })
                    }
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500"
                    placeholder="0.00"
                    min="0"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Type Ruimte
                  </label>
                  <select
                    value={ruimte.soort.code}
                    onChange={(e) =>
                      updateRuimte(index, {
                        soort: { code: e.target.value as 'VTK' | 'OVR' },
                        detailSoort: undefined,
                      })
                    }
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500"
                  >
                    <option value="VTK">Vertrek (kamer)</option>
                    <option value="OVR">Overige ruimte</option>
                  </select>
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Detail Type
                  </label>
                  <select
                    value={ruimte.detailSoort?.code || ''}
                    onChange={(e) =>
                      updateRuimte(index, {
                        detailSoort: e.target.value ? { code: e.target.value } : undefined,
                      })
                    }
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500"
                  >
                    <option value="">-- Selecteer --</option>
                    {ruimteTypes[ruimte.soort.code].map((type) => (
                      <option key={type.code} value={type.code}>
                        {type.name}
                      </option>
                    ))}
                  </select>
                </div>

                <div className="flex items-center space-x-4">
                  <label className="flex items-center">
                    <input
                      type="checkbox"
                      checked={ruimte.verwarmd || false}
                      onChange={(e) => updateRuimte(index, { verwarmd: e.target.checked })}
                      className="mr-2 h-4 w-4 text-primary-600 focus:ring-primary-500 border-gray-300 rounded"
                    />
                    <span className="text-sm text-gray-700">Verwarmd</span>
                  </label>

                  <label className="flex items-center">
                    <input
                      type="checkbox"
                      checked={ruimte.verkoeld || false}
                      onChange={(e) => updateRuimte(index, { verkoeld: e.target.checked })}
                      className="mr-2 h-4 w-4 text-primary-600 focus:ring-primary-500 border-gray-300 rounded"
                    />
                    <span className="text-sm text-gray-700">Verkoeld</span>
                  </label>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}

      <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
        <p className="text-sm text-blue-800">
          <strong>Tip:</strong> Voeg alle kamers en ruimtes toe. Vertrekken (VTK) zoals
          woonkamer, slaapkamer en keuken krijgen 1 punt per m². Overige ruimtes (OVR) zoals
          berging en zolder krijgen 0,75 punt per m².
        </p>
      </div>
    </div>
  );
};

export default RuimtesStep;

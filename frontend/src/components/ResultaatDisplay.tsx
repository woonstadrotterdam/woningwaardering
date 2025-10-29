import React, { useState } from 'react';
import { WoningwaarderingResultaat, FormData } from '../types';
import {
  FaCheckCircle,
  FaHome,
  FaFileDownload,
  FaChevronDown,
  FaChevronUp,
} from 'react-icons/fa';

interface Props {
  resultaat: WoningwaarderingResultaat;
  formData: FormData;
  onReset: () => void;
}

const ResultaatDisplay: React.FC<Props> = ({ resultaat, formData, onReset }) => {
  const [expandedGroep, setExpandedGroep] = useState<number | null>(null);

  const downloadJSON = () => {
    const data = {
      input: formData,
      output: resultaat,
      timestamp: new Date().toISOString(),
    };

    const blob = new Blob([JSON.stringify(data, null, 2)], {
      type: 'application/json',
    });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `woningwaardering-${formData.id}-${Date.now()}.json`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  const toggleGroep = (index: number) => {
    setExpandedGroep(expandedGroep === index ? null : index);
  };

  return (
    <div className="max-w-4xl mx-auto">
      {/* Header */}
      <div className="bg-green-600 text-white rounded-t-lg p-6">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <FaCheckCircle className="text-4xl" />
            <div>
              <h2 className="text-2xl font-bold">Berekening Voltooid!</h2>
              <p className="text-green-100">Woningwaardering voor {formData.id}</p>
            </div>
          </div>
          <FaHome className="text-5xl opacity-50" />
        </div>
      </div>

      {/* Hoofdresultaten */}
      <div className="bg-white border-x border-gray-300 p-6">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="text-center">
            <div className="text-4xl font-bold text-primary-600">
              {resultaat.punten?.toFixed(0) || 0}
            </div>
            <div className="text-gray-600 mt-2">WWS Punten</div>
          </div>

          <div className="text-center">
            <div className="text-4xl font-bold text-green-600">
              € {resultaat.maximale_huur?.toFixed(2) || 0}
            </div>
            <div className="text-gray-600 mt-2">Maximale Huur (basis)</div>
          </div>

          {resultaat.maximale_huur_inclusief_opslag && (
            <div className="text-center">
              <div className="text-4xl font-bold text-green-700">
                € {resultaat.maximale_huur_inclusief_opslag.toFixed(2)}
              </div>
              <div className="text-gray-600 mt-2">
                Maximale Huur (incl. opslag)
                {resultaat.opslagpercentage && (
                  <span className="text-sm block">
                    (+{resultaat.opslagpercentage}%)
                  </span>
                )}
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Stelsel Info */}
      {resultaat.stelsel && (
        <div className="bg-gray-50 border-x border-gray-300 p-4">
          <p className="text-sm text-gray-700">
            <strong>Stelsel:</strong> {resultaat.stelsel.naam} ({resultaat.stelsel.code})
          </p>
        </div>
      )}

      {/* Groepen Details */}
      {resultaat.groepen && resultaat.groepen.length > 0 && (
        <div className="bg-white border-x border-gray-300 p-6">
          <h3 className="text-xl font-semibold text-gray-800 mb-4">
            Details per Stelselgroep
          </h3>

          <div className="space-y-3">
            {resultaat.groepen.map((groep, index) => (
              <div key={index} className="border border-gray-300 rounded-lg overflow-hidden">
                {/* Groep Header */}
                <button
                  onClick={() => toggleGroep(index)}
                  className="w-full flex items-center justify-between p-4 bg-gray-50 hover:bg-gray-100 transition-colors"
                >
                  <div className="flex items-center gap-3">
                    <div className="text-left">
                      <div className="font-semibold text-gray-800">
                        {groep.criteriumGroep?.stelselgroep?.naam || 'Onbekend'}
                      </div>
                      <div className="text-sm text-gray-600">
                        {groep.criteriumGroep?.stelselgroep?.code}
                      </div>
                    </div>
                  </div>

                  <div className="flex items-center gap-4">
                    <div className="text-right">
                      <div className="text-lg font-bold text-primary-600">
                        {groep.punten?.toFixed(2) || 0} punten
                      </div>
                      {groep.opslagpercentage && (
                        <div className="text-sm text-gray-600">
                          +{groep.opslagpercentage}% opslag
                        </div>
                      )}
                    </div>
                    {expandedGroep === index ? (
                      <FaChevronUp className="text-gray-600" />
                    ) : (
                      <FaChevronDown className="text-gray-600" />
                    )}
                  </div>
                </button>

                {/* Groep Details (uitklapbaar) */}
                {expandedGroep === index && groep.woningwaarderingen && (
                  <div className="p-4 bg-white border-t border-gray-300">
                    <table className="w-full text-sm">
                      <thead>
                        <tr className="border-b border-gray-300">
                          <th className="text-left py-2">Criterium</th>
                          <th className="text-right py-2">Aantal</th>
                          <th className="text-right py-2">Punten</th>
                        </tr>
                      </thead>
                      <tbody>
                        {groep.woningwaarderingen.map((item, itemIndex) => (
                          <tr key={itemIndex} className="border-b border-gray-200">
                            <td className="py-2">
                              {item.criterium?.naam || 'Onbekend'}
                              {item.criterium?.meeteenheid && (
                                <span className="text-gray-500 ml-1 text-xs">
                                  ({item.criterium.meeteenheid.naam})
                                </span>
                              )}
                            </td>
                            <td className="text-right py-2">
                              {item.aantal?.toFixed(2) || '-'}
                            </td>
                            <td className="text-right py-2 font-semibold">
                              {item.punten?.toFixed(2) || 0}
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Acties */}
      <div className="bg-white rounded-b-lg border border-gray-300 p-6 flex justify-between">
        <button
          onClick={onReset}
          className="px-6 py-3 bg-gray-600 text-white rounded-lg hover:bg-gray-700 flex items-center gap-2"
        >
          <FaHome /> Nieuwe Berekening
        </button>

        <button
          onClick={downloadJSON}
          className="px-6 py-3 bg-primary-600 text-white rounded-lg hover:bg-primary-700 flex items-center gap-2"
        >
          <FaFileDownload /> Download JSON
        </button>
      </div>

      {/* Footer info */}
      <div className="mt-6 bg-blue-50 border border-blue-200 rounded-lg p-4">
        <p className="text-sm text-blue-800">
          <strong>Let op:</strong> Deze berekening is gebaseerd op het Woningwaarderingsstelsel
          voor zelfstandige woonruimten. De werkelijke maximale huurprijs kan afwijken
          afhankelijk van specifieke omstandigheden. Raadpleeg altijd de officiële documentatie
          van de Huurcommissie voor definitieve informatie.
        </p>
      </div>
    </div>
  );
};

export default ResultaatDisplay;

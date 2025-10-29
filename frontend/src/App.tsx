import React, { useState } from 'react';
import WoningForm from './components/WoningForm';
import { woningTemplates, WoningTemplate } from './templates/examples';
import { FaHome, FaInfoCircle } from 'react-icons/fa';

function App() {
  const [showTemplates, setShowTemplates] = useState(false);
  const [selectedTemplate, setSelectedTemplate] = useState<WoningTemplate | null>(null);
  const [showInfo, setShowInfo] = useState(false);

  const handleTemplateSelect = (template: WoningTemplate) => {
    setSelectedTemplate(template);
    setShowTemplates(false);
  };

  const handleStartEmpty = () => {
    setSelectedTemplate(null);
    setShowTemplates(false);
  };

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Header */}
      <header className="bg-primary-700 text-white shadow-lg">
        <div className="container mx-auto px-4 py-6">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <FaHome className="text-3xl" />
              <div>
                <h1 className="text-2xl font-bold">Woningwaardering Calculator</h1>
                <p className="text-primary-100 text-sm">
                  Bereken de WWS punten en maximale huurprijs
                </p>
              </div>
            </div>
            <button
              onClick={() => setShowInfo(!showInfo)}
              className="p-2 hover:bg-primary-600 rounded-lg transition-colors"
            >
              <FaInfoCircle className="text-2xl" />
            </button>
          </div>
        </div>
      </header>

      {/* Info Panel */}
      {showInfo && (
        <div className="bg-blue-50 border-b border-blue-200">
          <div className="container mx-auto px-4 py-6">
            <h2 className="text-lg font-semibold text-blue-900 mb-3">
              Over deze Calculator
            </h2>
            <div className="text-sm text-blue-800 space-y-2">
              <p>
                Deze calculator berekent de woningwaardering volgens het{' '}
                <strong>Woningwaarderingsstelsel (WWS)</strong> voor zelfstandige
                woonruimten. Het WWS bepaalt het maximale huurbedrag dat een verhuurder mag
                vragen voor een sociale huurwoning.
              </p>
              <p>
                De berekening is gebaseerd op verschillende factoren zoals oppervlakte,
                energielabel, WOZ-waarde, en voorzieningen. Het resultaat geeft het aantal
                WWS-punten en de bijbehorende maximale huurprijs.
              </p>
              <p className="font-semibold">
                Let op: Deze calculator is bedoeld als hulpmiddel. Voor officiële berekeningen
                dient u contact op te nemen met de Huurcommissie.
              </p>
            </div>
          </div>
        </div>
      )}

      {/* Main Content */}
      <main className="container mx-auto px-4 py-8">
        {showTemplates ? (
          /* Template Selector */
          <div className="max-w-4xl mx-auto">
            <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
              <h2 className="text-2xl font-bold text-gray-800 mb-4">
                Kies een sjabloon of start leeg
              </h2>
              <p className="text-gray-600 mb-6">
                Selecteer een voorbeeldwoning om snel te beginnen, of start met een lege
                woning.
              </p>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
                {woningTemplates.map((template) => (
                  <button
                    key={template.id}
                    onClick={() => handleTemplateSelect(template)}
                    className="text-left p-4 border-2 border-gray-300 rounded-lg hover:border-primary-600 hover:bg-primary-50 transition-all"
                  >
                    <h3 className="font-semibold text-lg text-gray-800 mb-2">
                      {template.naam}
                    </h3>
                    <p className="text-sm text-gray-600">{template.beschrijving}</p>
                    <div className="mt-3 text-xs text-gray-500">
                      <span className="inline-block bg-gray-200 rounded px-2 py-1 mr-2">
                        {template.data.ruimten?.length || 0} ruimtes
                      </span>
                      <span className="inline-block bg-gray-200 rounded px-2 py-1 mr-2">
                        {template.data.bouwjaar}
                      </span>
                      <span className="inline-block bg-gray-200 rounded px-2 py-1">
                        {template.data.energieprestaties?.[0]?.label || 'Geen label'}
                      </span>
                    </div>
                  </button>
                ))}
              </div>

              <button
                onClick={handleStartEmpty}
                className="w-full p-4 bg-gray-600 text-white rounded-lg hover:bg-gray-700 font-semibold"
              >
                Start met Lege Woning
              </button>
            </div>
          </div>
        ) : (
          /* Form */
          <div>
            <div className="flex justify-end mb-4">
              <button
                onClick={() => setShowTemplates(true)}
                className="px-4 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700"
              >
                Laad Sjabloon
              </button>
            </div>
            <WoningForm key={selectedTemplate?.id || 'empty'} />
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="bg-gray-800 text-gray-300 mt-16">
        <div className="container mx-auto px-4 py-6">
          <div className="text-center text-sm">
            <p>
              Woningwaardering Calculator - Gebaseerd op het Woningwaarderingsstelsel voor
              zelfstandige woonruimten
            </p>
            <p className="mt-2">
              <a
                href="https://www.huurcommissie.nl"
                target="_blank"
                rel="noopener noreferrer"
                className="text-primary-400 hover:text-primary-300"
              >
                Meer informatie bij de Huurcommissie
              </a>
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;

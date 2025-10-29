import React, { useState } from 'react';
import { FormData, WoningwaarderingResultaat } from '../types';
import { woningwaarderingApi } from '../services/api';
import BasisInfoStep from './steps/BasisInfoStep';
import RuimtesStep from './steps/RuimtesStep';
import EnergieprestatieStep from './steps/EnergieprestatieStep';
import WOZStep from './steps/WOZStep';
import OverzichtStep from './steps/OverzichtStep';
import ResultaatDisplay from './ResultaatDisplay';
import { FaHome, FaDoorOpen, FaBolt, FaEuroSign, FaClipboardList } from 'react-icons/fa';

const steps = [
  { id: 1, name: 'Basis Info', icon: FaHome },
  { id: 2, name: 'Ruimtes', icon: FaDoorOpen },
  { id: 3, name: 'Energie', icon: FaBolt },
  { id: 4, name: 'WOZ Waarde', icon: FaEuroSign },
  { id: 5, name: 'Overzicht', icon: FaClipboardList },
];

const WoningForm: React.FC = () => {
  const [currentStep, setCurrentStep] = useState(1);
  const [formData, setFormData] = useState<FormData>({
    id: `WONING-${Date.now()}`,
    ruimten: [],
  });
  const [resultaat, setResultaat] = useState<WoningwaarderingResultaat | null>(null);
  const [isCalculating, setIsCalculating] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const updateFormData = (updates: Partial<FormData>) => {
    setFormData((prev) => ({ ...prev, ...updates }));
  };

  const handleNext = () => {
    if (currentStep < steps.length) {
      setCurrentStep(currentStep + 1);
    }
  };

  const handlePrevious = () => {
    if (currentStep > 1) {
      setCurrentStep(currentStep - 1);
    }
  };

  const handleCalculate = async () => {
    setIsCalculating(true);
    setError(null);

    try {
      const result = await woningwaarderingApi.bereken(formData, formData.peildatum);
      setResultaat(result);
    } catch (err: any) {
      console.error('Berekening fout:', err);
      setError(err.response?.data?.detail || 'Er is een fout opgetreden bij het berekenen');
    } finally {
      setIsCalculating(false);
    }
  };

  const handleReset = () => {
    setFormData({
      id: `WONING-${Date.now()}`,
      ruimten: [],
    });
    setResultaat(null);
    setError(null);
    setCurrentStep(1);
  };

  if (resultaat) {
    return (
      <ResultaatDisplay
        resultaat={resultaat}
        formData={formData}
        onReset={handleReset}
      />
    );
  }

  const renderStep = () => {
    switch (currentStep) {
      case 1:
        return <BasisInfoStep formData={formData} updateFormData={updateFormData} />;
      case 2:
        return <RuimtesStep formData={formData} updateFormData={updateFormData} />;
      case 3:
        return <EnergieprestatieStep formData={formData} updateFormData={updateFormData} />;
      case 4:
        return <WOZStep formData={formData} updateFormData={updateFormData} />;
      case 5:
        return <OverzichtStep formData={formData} />;
      default:
        return null;
    }
  };

  return (
    <div className="max-w-4xl mx-auto">
      {/* Progress Indicator */}
      <div className="mb-8">
        <div className="flex justify-between items-center">
          {steps.map((step, index) => (
            <React.Fragment key={step.id}>
              <div className="flex flex-col items-center">
                <div
                  className={`w-12 h-12 rounded-full flex items-center justify-center ${
                    currentStep >= step.id
                      ? 'bg-primary-600 text-white'
                      : 'bg-gray-300 text-gray-600'
                  }`}
                >
                  <step.icon className="w-5 h-5" />
                </div>
                <span className="text-xs mt-2 text-center">{step.name}</span>
              </div>
              {index < steps.length - 1 && (
                <div
                  className={`flex-1 h-1 mx-2 ${
                    currentStep > step.id ? 'bg-primary-600' : 'bg-gray-300'
                  }`}
                />
              )}
            </React.Fragment>
          ))}
        </div>
      </div>

      {/* Form Step Content */}
      <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
        {renderStep()}
      </div>

      {/* Error Display */}
      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          <strong className="font-bold">Fout: </strong>
          <span>{error}</span>
        </div>
      )}

      {/* Navigation Buttons */}
      <div className="flex justify-between">
        <button
          onClick={handlePrevious}
          disabled={currentStep === 1}
          className="px-6 py-2 bg-gray-300 text-gray-700 rounded-lg hover:bg-gray-400 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          Vorige
        </button>

        {currentStep < steps.length ? (
          <button
            onClick={handleNext}
            className="px-6 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700"
          >
            Volgende
          </button>
        ) : (
          <button
            onClick={handleCalculate}
            disabled={isCalculating}
            className="px-6 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {isCalculating ? 'Berekenen...' : 'Bereken Woningwaardering'}
          </button>
        )}
      </div>
    </div>
  );
};

export default WoningForm;

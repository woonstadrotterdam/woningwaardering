import React from 'react';
import { FormData } from '../../types';
import { FaCheckCircle, FaExclamationTriangle } from 'react-icons/fa';

interface Props {
  formData: FormData;
}

const OverzichtStep: React.FC<Props> = ({ formData }) => {
  const hasRuimten = formData.ruimten && formData.ruimten.length > 0;
  const hasEnergielabel = formData.energieprestaties?.[0]?.label;
  const hasWOZ = formData.wozEenheden?.[0]?.vastgesteldeWaarde;

  const totalOppervlakte = formData.ruimten?.reduce(
    (sum, ruimte) => sum + (ruimte.oppervlakte || 0),
    0
  ) || 0;

  const verwarmdeRuimten = formData.ruimten?.filter((r) => r.verwarmd).length || 0;

  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold text-gray-800 mb-4">Overzicht</h2>

      <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 mb-6">
        <p className="text-sm text-blue-800">
          Controleer de ingevoerde gegevens voordat je de woningwaardering berekent. Je kunt
          altijd terug naar eerdere stappen om aanpassingen te maken.
        </p>
      </div>

      {/* Basis Info */}
      <div className="border border-gray-300 rounded-lg p-4">
        <h3 className="text-lg font-semibold text-gray-800 mb-3">Basis Informatie</h3>
        <div className="grid grid-cols-2 gap-4 text-sm">
          <div>
            <span className="text-gray-600">Woning ID:</span>
            <span className="ml-2 font-medium">{formData.id}</span>
          </div>
          {formData.bouwjaar && (
            <div>
              <span className="text-gray-600">Bouwjaar:</span>
              <span className="ml-2 font-medium">{formData.bouwjaar}</span>
            </div>
          )}
          {formData.adres?.straatnaam && (
            <div className="col-span-2">
              <span className="text-gray-600">Adres:</span>
              <span className="ml-2 font-medium">
                {formData.adres.straatnaam} {formData.adres.huisnummer}
                {formData.adres.huisnummerToevoeging}, {formData.adres.postcode}
              </span>
            </div>
          )}
          {formData.adresseerbaarObjectBasisregistratie?.bagIdentificatie && (
            <div className="col-span-2">
              <span className="text-gray-600">BAG ID:</span>
              <span className="ml-2 font-medium">
                {formData.adresseerbaarObjectBasisregistratie.bagIdentificatie}
              </span>
            </div>
          )}
        </div>
      </div>

      {/* Ruimtes */}
      <div className="border border-gray-300 rounded-lg p-4">
        <div className="flex items-center justify-between mb-3">
          <h3 className="text-lg font-semibold text-gray-800">Ruimtes</h3>
          {hasRuimten ? (
            <FaCheckCircle className="text-green-600" />
          ) : (
            <FaExclamationTriangle className="text-yellow-600" />
          )}
        </div>

        {hasRuimten ? (
          <>
            <div className="grid grid-cols-3 gap-4 mb-4 text-sm">
              <div>
                <span className="text-gray-600">Aantal ruimtes:</span>
                <span className="ml-2 font-medium">{formData.ruimten?.length}</span>
              </div>
              <div>
                <span className="text-gray-600">Totale oppervlakte:</span>
                <span className="ml-2 font-medium">{totalOppervlakte.toFixed(2)} m²</span>
              </div>
              <div>
                <span className="text-gray-600">Verwarmde ruimtes:</span>
                <span className="ml-2 font-medium">{verwarmdeRuimten}</span>
              </div>
            </div>

            <div className="space-y-2">
              {formData.ruimten?.map((ruimte, index) => (
                <div key={ruimte.id} className="text-sm bg-gray-50 p-2 rounded">
                  <span className="font-medium">{ruimte.naam || `Ruimte ${index + 1}`}</span>
                  <span className="text-gray-600 ml-2">
                    ({ruimte.oppervlakte} m² - {ruimte.soort.code})
                    {ruimte.verwarmd && ' 🔥'}
                  </span>
                </div>
              ))}
            </div>
          </>
        ) : (
          <p className="text-sm text-yellow-700">
            Geen ruimtes toegevoegd. Het is sterk aanbevolen om minimaal de hoofdruimtes toe
            te voegen voor een accurate berekening.
          </p>
        )}
      </div>

      {/* Energieprestatie */}
      <div className="border border-gray-300 rounded-lg p-4">
        <div className="flex items-center justify-between mb-3">
          <h3 className="text-lg font-semibold text-gray-800">Energieprestatie</h3>
          {hasEnergielabel ? (
            <FaCheckCircle className="text-green-600" />
          ) : (
            <FaExclamationTriangle className="text-yellow-600" />
          )}
        </div>

        {hasEnergielabel ? (
          <div className="text-sm">
            <span className="text-gray-600">Energielabel:</span>
            <span className="ml-2 font-medium text-lg">
              {formData.energieprestaties?.[0]?.label}
            </span>
            {formData.energieprestaties?.[0]?.soort?.code && (
              <>
                <br />
                <span className="text-gray-600">Type:</span>
                <span className="ml-2 font-medium">
                  {formData.energieprestaties[0].soort.code}
                </span>
              </>
            )}
          </div>
        ) : (
          <p className="text-sm text-yellow-700">
            Geen energielabel opgegeven. Dit kan punten kosten of opleveren.
          </p>
        )}
      </div>

      {/* WOZ Waarde */}
      <div className="border border-gray-300 rounded-lg p-4">
        <div className="flex items-center justify-between mb-3">
          <h3 className="text-lg font-semibold text-gray-800">WOZ Waarde</h3>
          {hasWOZ ? (
            <FaCheckCircle className="text-green-600" />
          ) : (
            <FaExclamationTriangle className="text-yellow-600" />
          )}
        </div>

        {hasWOZ ? (
          <div className="text-sm">
            <span className="text-gray-600">Vastgestelde waarde:</span>
            <span className="ml-2 font-medium text-lg">
              € {formData.wozEenheden?.[0]?.vastgesteldeWaarde.toLocaleString('nl-NL')}
            </span>
            {formData.wozEenheden?.[0]?.waardepeildatum && (
              <>
                <br />
                <span className="text-gray-600">Peildatum:</span>
                <span className="ml-2 font-medium">
                  {new Date(
                    formData.wozEenheden[0].waardepeildatum
                  ).toLocaleDateString('nl-NL')}
                </span>
              </>
            )}
          </div>
        ) : (
          <p className="text-sm text-yellow-700">
            Geen WOZ-waarde opgegeven. De WOZ-waarde kan extra punten opleveren.
          </p>
        )}
      </div>

      {/* Waarschuwingen */}
      {(!hasRuimten || !hasEnergielabel || !hasWOZ) && (
        <div className="bg-yellow-50 border border-yellow-300 rounded-lg p-4">
          <h4 className="font-semibold text-yellow-800 mb-2">Let op:</h4>
          <ul className="text-sm text-yellow-800 list-disc list-inside space-y-1">
            {!hasRuimten && <li>Er zijn geen ruimtes toegevoegd</li>}
            {!hasEnergielabel && <li>Er is geen energielabel opgegeven</li>}
            {!hasWOZ && <li>Er is geen WOZ-waarde opgegeven</li>}
          </ul>
          <p className="text-sm text-yellow-800 mt-2">
            De berekening kan wel worden uitgevoerd, maar is mogelijk niet volledig of
            accuraat.
          </p>
        </div>
      )}

      <div className="bg-green-50 border border-green-300 rounded-lg p-4">
        <p className="text-sm text-green-800">
          <strong>Klaar voor berekening!</strong> Klik op "Bereken Woningwaardering" om de
          WWS punten en maximale huurprijs te berekenen.
        </p>
      </div>
    </div>
  );
};

export default OverzichtStep;

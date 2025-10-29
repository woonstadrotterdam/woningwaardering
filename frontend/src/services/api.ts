// API service voor communicatie met de backend
import axios from 'axios';
import { EenhedenEenheid, WoningwaarderingResultaat } from '../types';

const API_BASE_URL = '/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const woningwaarderingApi = {
  /**
   * Bereken de woningwaardering
   */
  async bereken(
    eenheid: EenhedenEenheid,
    peildatum?: string
  ): Promise<WoningwaarderingResultaat> {
    const response = await api.post<WoningwaarderingResultaat>(
      '/bereken',
      eenheid,
      {
        params: peildatum ? { peildatum } : undefined,
      }
    );
    return response.data;
  },

  /**
   * Health check
   */
  async health(): Promise<{ status: string }> {
    const response = await api.get('/health');
    return response.data;
  },

  /**
   * Haal referentiedata op
   */
  async getReferentiedata() {
    const [ruimtesoorten, detailsoorten, energielabels] = await Promise.all([
      api.get('/referentiedata/ruimtesoorten'),
      api.get('/referentiedata/ruimte-detailsoorten'),
      api.get('/referentiedata/energielabels'),
    ]);

    return {
      ruimtesoorten: ruimtesoorten.data,
      detailsoorten: detailsoorten.data,
      energielabels: energielabels.data,
    };
  },
};

export default api;

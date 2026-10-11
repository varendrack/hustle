/**
 * Cloudflare Worker Proxy Sécurisé pour Google Gemini AI
 * Protège la clé d'API (stockée dans les Secrets Cloudflare : GEMINI_API_KEY)
 * et sert les fichiers statiques de Jeux_Interactifs.
 */

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    // Endpoint API pour la génération d'exercices avec Gemini
    if (url.pathname === '/api/gemini') {
      // Gestion CORS Preflight (OPTIONS)
      if (request.method === 'OPTIONS') {
        return new Response(null, {
          status: 204,
          headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '86400',
          },
        });
      }

      if (request.method !== 'POST') {
        return new Response(JSON.stringify({ error: 'Méthode non autorisée. Utilisez POST.' }), {
          status: 405,
          headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
          },
        });
      }

      const apiKey = env.GEMINI_API_KEY;
      if (!apiKey) {
        return new Response(
          JSON.stringify({
            error:
              "La variable secrète GEMINI_API_KEY n'est pas encore configurée dans les paramètres de votre Worker Cloudflare.",
          }),
          {
            status: 500,
            headers: {
              'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': '*',
            },
          }
        );
      }

      try {
        const body = await request.json();
        const promptText = body.prompt;
        if (!promptText || typeof promptText !== 'string') {
          return new Response(JSON.stringify({ error: 'Le champ "prompt" est requis.' }), {
            status: 400,
            headers: {
              'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': '*',
            },
          });
        }

        // Modèles Gemini testés par ordre de rapidité / quota
        const models = ['gemini-2.5-flash', 'gemini-2.0-flash', 'gemini-1.5-flash'];
        let lastError = null;

        for (const model of models) {
          try {
            const googleUrl = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${apiKey}`;
            const geminiRes = await fetch(googleUrl, {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                contents: [{ parts: [{ text: promptText }] }],
                generationConfig: {
                  temperature: 0.7,
                  responseMimeType: 'application/json',
                },
              }),
            });

            if (!geminiRes.ok) {
              const errData = await geminiRes.json().catch(() => ({}));
              throw new Error(errData.error?.message || `Erreur API Gemini (${geminiRes.status})`);
            }

            const data = await geminiRes.json();
            const rawText = data.candidates?.[0]?.content?.parts?.[0]?.text;
            if (!rawText) throw new Error('Réponse vide de Gemini');

            const parsed = JSON.parse(rawText);
            return new Response(JSON.stringify(parsed), {
              status: 200,
              headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
              },
            });
          } catch (err) {
            lastError = err;
          }
        }

        return new Response(
          JSON.stringify({
            error: lastError?.message || 'Impossible de joindre les modèles Gemini.',
          }),
          {
            status: 502,
            headers: {
              'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': '*',
            },
          }
        );
      } catch (err) {
        return new Response(JSON.stringify({ error: err.message || 'Erreur interne' }), {
          status: 400,
          headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
          },
        });
      }
    }

    // Pour toute autre requête, déléguer aux assets statiques (HTML, CSS, JS, sons, etc.)
    return env.ASSETS.fetch(request);
  },
};

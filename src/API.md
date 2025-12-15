 ***

### Analisar depressão

- Método: POST
- URL: https://api.dpy.me/
- Parâmetros:

  - body:
    ``` json
    {
        "age": 25,
        "academic_pressure": 2,
        "study_satisfaction": 1,
        "dietary_habits": 1,
        "degree": 2,
        "suicidal_thoughts": 1,
        "workstudy_hours": 1,
        "financial_stress": 1
    }
    ```

- Resposta:
  - Sucesso (200 OK)

    ``` json
    {
    	"depression": false,
    	"success": true
    }

    ```

  - Erro (400)
    ```json
    {
      "error": "Field degree must be a number"
    }
    ```
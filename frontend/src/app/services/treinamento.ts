import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class TreinamentoService {
  private apiUrl = 'http://localhost:8000/api/treinamentos/';

  constructor(private http: HttpClient) {}

  listarTreinamentos(): Observable<any[]> {
    const token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Authorization': `Token ${token}`
    });
    return this.http.get<any>(this.apiUrl, { headers }).pipe(
      map(res => {
        // se vier paginado, usa res.results, se não, usa o array direto
        return res.results || res;
      })
    );
  }

  criar(data: any): Observable<any> {
    const token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Authorization': `Token ${token}`
    });
    return this.http.post(this.apiUrl, data, { headers });
  }
}


import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

export interface Turma {
  id: number;
  nome: string;
}

@Injectable({
  providedIn: 'root'
})
export class TurmaService {
  private apiUrl = 'http://localhost:8000/api/turmas/';

  constructor(private http: HttpClient) {}

  listarTurmas(treinamentoId: number): Observable<any[]> {
    const token = localStorage.getItem('token');
    const headers = new HttpHeaders({ 'Authorization': `Token ${token}` });
    return this.http.get<any>(`${this.apiUrl}?treinamento=${treinamentoId}`, { headers })
      .pipe(
        map(res => res.results || res)
      );
  }

  criarTurma(turma: any): Observable<any> {
    const token = localStorage.getItem('token');
    const headers = new HttpHeaders({ Authorization: `Token ${token}` });
    return this.http.post<any>(this.apiUrl, turma, { headers });
  }
}


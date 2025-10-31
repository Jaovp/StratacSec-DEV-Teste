import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class RecursoService {
  private apiUrl = 'http://localhost:8000/api/recursos/';

  constructor(private http: HttpClient) {}
  
  listarRecursos(turmaId: number): Observable<any[]> {
    const token = localStorage.getItem('token') || '';
    const headers = new HttpHeaders({ 'Authorization': `Token ${token}` });

    return this.http.get<any>(`${this.apiUrl}?turma=${turmaId}`, { headers }).pipe(
      map(res => res.results || res)
    );
  }

  criarRecurso(recurso: any): Observable<any> {
    const token = localStorage.getItem('token') || '';
    const headers = new HttpHeaders({ 'Authorization': `Token ${token}` });
    return this.http.post<any>(this.apiUrl, recurso, { headers });
  }
}

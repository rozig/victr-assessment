import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from './../../environments/environment';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private BASE_URL = environment.apiUrl;
  private headers = new HttpHeaders({'Content-Type': 'application/json'});
  constructor(private http: HttpClient) { }

  getRepositories(page: number = 1) {
    return this.http.get(`${this.BASE_URL}/github/?page=${page}`, {headers: this.headers});
  }
}

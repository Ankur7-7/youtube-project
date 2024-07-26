import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class CommentsService {

  private url: string="http://127.0.0.1:5000";

  constructor(private http: HttpClient) { }

  fetch_comments(search: string): Observable<any>{
    return this.http.get(`${this.url}/comments?search=${search}`);
  }
}

import { Component, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {environment} from '../../environments/environment';
import {IQuestion, IAnswer, IAnswerResponse} from '../BaseClasses/Interfaces/interfaces';
import {Observable} from 'rxjs';

@Component({
  selector: 'app-interactive-helper',
  templateUrl: './interactive-helper.component.html',
  styleUrls: ['./interactive-helper.component.less']
})
export class InteractiveHelperComponent implements OnInit {
  private API_URL = environment.API_URL;
  public questions: IQuestion[];
  public currentQuestion: IQuestion;
  public showUpload = false;
  private currentQuestionIndex = 0;
  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.getQuestions().subscribe((questions) => {
      this.questions = questions;
      this.currentQuestion = questions[0];
    });
  }

  private getQuestions(): Observable<IQuestion[]> {
  return this.http.get<IQuestion[]>(`${this.API_URL}/get_questions`);
  }

  public changeQuestion() {
    this.currentQuestionIndex += 1;
    if (this.currentQuestionIndex === this.questions.length) {
      this.showUpload = true;
      return;
    }
    setTimeout(() => this.currentQuestion = this.questions[this.currentQuestionIndex], 700);
  }
}

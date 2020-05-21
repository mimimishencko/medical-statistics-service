import { Component, OnInit } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {environment} from '../../environments/environment';
import {IQuestion, IAnswer, IAnswerResponse} from '../BaseClasses/Interfaces/interfaces';
import {Observable} from 'rxjs';
import {FormControl, FormGroup} from '@angular/forms';
import { saveAs } from 'file-saver';
import {Router} from '@angular/router';

@Component({
  selector: 'app-interactive-helper',
  templateUrl: './interactive-helper.component.html',
  styleUrls: ['./interactive-helper.component.less']
})
export class InteractiveHelperComponent implements OnInit {
  private API_URL = environment.API_URL;
  public questions: IQuestion[];
  public form: FormGroup;
  public currentQuestion: IQuestion;
  public showUpload = false;
  public helperData: IAnswerResponse[] = [];
  private currentQuestionIndex = 0;
  constructor(private http: HttpClient, private router: Router) {
    this.form = new FormGroup({
      file: new FormControl(''),
      helper_data: new FormControl(''),
    });
  }

  ngOnInit() {
    this.getQuestions().subscribe((questions) => {
      this.questions = questions;
      this.currentQuestion = questions[0];
    });
  }

  private getQuestions(): Observable<IQuestion[]> {
  return this.http.get<IQuestion[]>(`${this.API_URL}/get_questions`);
  }

  public changeQuestion(answerId) {
    this.helperData.push({question_code_name: this.currentQuestion.code_name, answer_id: answerId});
    if (this.currentQuestion.code_name === 'sample_count' && answerId === 1) {
      this.showUpload = true;
      return;
    }
    if (this.currentQuestion.code_name === 'sample_count' && answerId === 2) {
      this.questions = this.questions.filter(question => question.code_name !== 'independent_more_samples');
    }
    if (this.currentQuestion.code_name === 'sample_count' && answerId === 3) {
      this.questions = this.questions.filter(question => question.code_name !== 'independent_two_samples');
    }
    if (this.currentQuestion.code_name === 'analysis_goal' && answerId === 1) {
      this.showUpload = true;
      return;
    }
    this.currentQuestionIndex += 1;
    if (this.currentQuestionIndex === this.questions.length) {
      this.showUpload = true;
      return;
    }
    setTimeout(() => this.currentQuestion = this.questions[this.currentQuestionIndex], 700);
  }

  public onPictureSelected(event) {
    this.form.patchValue({ file: event.target.files[0] });
    this.form.patchValue( {helper_data: this.helperData});
    console.log(this.form.get('helper_data').value);
    const formData = new FormData();
    formData.append('file', this.form.get('file').value);
    formData.append('helper_data', JSON.stringify(this.form.get('helper_data').value));
    this.http.post('http://localhost:5000/', formData,
      {headers: new HttpHeaders({enctype: 'multipart/form-data', Accept: 'application/json'}),
      responseType: 'blob'} ).subscribe((report) => {
      const mediaType = 'application/pdf';
      const blob = new Blob([report], {type: mediaType});
      const filename = 'report.pdf';
      saveAs(blob, filename);
      this.router.navigate(['/']);
    });
  }
}

export interface IQuestion {
  id: number;
  code_name: string;
  question: string;
  answers: IAnswer[];
  description?: string[];
  }


export interface IAnswer {
  id: number;
  answer: string;
}

export interface IAnswerResponse {
  question_code_name: string;
  answer_id: number;
}

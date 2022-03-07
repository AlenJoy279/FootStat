package com.example.footstattest.models;

import android.content.Context;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import androidx.annotation.NonNull;

import com.example.footstattest.R;
import com.example.footstattest.models.jaime.Table;

import java.util.ArrayList;

/* This class allows us to adapt the list of Table objects into a listView
It takes the context, the custom layout file for the list columns and a list of table objects as inputs
 */
public class TeamListAdapter extends ArrayAdapter<Table> {

    public static final String TAG = "TeamListAdapter";

    int res;
    private Context cContext;

    public TeamListAdapter(@NonNull Context context, int resource, @NonNull ArrayList<Table> objects) {
        super(context, resource, objects);
        cContext = context;
        res = resource;
    }

    @NonNull
    @Override
    public View getView(int position, View convertView, ViewGroup parent) {

        String name = getItem(position).getName();
        Log.d(TAG, "getView: " + getItem(position).getPosition());
        int pos = getItem(position).getPosition();
        int wins = getItem(position).getWon();
        int draws = getItem(position).getDraw();
        int loss = getItem(position).getLost();

        Table table = new Table(pos,  wins, draws, loss, name);

        LayoutInflater inflater = LayoutInflater.from(cContext);
        convertView = inflater.inflate(res, parent, false);

        TextView teamName = (TextView) convertView.findViewById(R.id.text_j_team);
        TextView teamPos = (TextView) convertView.findViewById(R.id.text_j_pos);
        TextView teamWin = (TextView) convertView.findViewById(R.id.text_j_win);
        TextView teamDraw = (TextView) convertView.findViewById(R.id.text_j_draw);
        TextView teamLoss = (TextView) convertView.findViewById(R.id.text_j_loss);

        teamName.setText(name);
        teamPos.setText(String.valueOf(pos));
        teamWin.setText(String.valueOf(wins));
        teamDraw.setText(String.valueOf(draws));
        teamLoss.setText(String.valueOf(loss));

        return convertView;


    }
}
